# Copyright 2015 Google Inc. All Rights Reserved.

"""Upgrade cluster command."""
import argparse

from googlecloudapis.apitools.base import py as apitools_base
from googlecloudsdk.calliope import base
from googlecloudsdk.calliope import exceptions
from googlecloudsdk.container.lib import util
from googlecloudsdk.core import log


@base.Hidden  # Hidden until upgrades are official
class Upgrade(base.Command):
  """Upgrade an existing cluster for running containers."""

  @staticmethod
  def Args(parser):
    """Register flags for this command.

    Args:
      parser: An argparse.ArgumentParser-like object. It is mocked out in order
          to capture some information, but behaves like an ArgumentParser.
    """
    parser.add_argument(
        'name',
        metavar='NAME',
        help='The name of the cluster to upgrade.')
    parser.add_argument(
        '--cluster-version',
        help='The kubernetes release version to change the cluster to.'
        ' Omit to upgrade to the latest version offered by the server.')
    parser.add_argument(
        '--master',
        help=argparse.SUPPRESS,
        action='store_true')
    parser.add_argument(
        '--no-wait',
        dest='wait',
        action='store_false',
        help='Return after issuing upgrade request without polling the'
        ' operation for completion.')

  # TODO(user): The preference now is to throw util.Error directly (see
  # comment in cl/93364826). Change this throughout sdk/container/...
  @exceptions.RaiseToolExceptionInsteadOf(util.Error)
  def Run(self, args):
    """This is what gets called when the user runs this command.

    Args:
      args: an argparse namespace. All the arguments that were provided to this
        command invocation.

    Returns:
      Some value that we want to have printed later.
    """
    client = self.context['container_client']
    messages = self.context['container_messages']

    if not hasattr(client.projects_zones_clusters, 'Update'):
      raise util.Error('Upgrade requires a v1beta2 client.')

    ref = util.ParseCluster(args.name, self.context)

    # Make sure it exists (will raise appropriate error if not)
    util.DescribeCluster(ref, self.context)

    if args.cluster_version:
      version = messages.ClusterVersion(clusterVersion=args.cluster_version)
    else:
      version = messages.ClusterVersion()

    if args.master:
      update = messages.ClusterUpdate(desiredMasterVersion=version)
    else:
      update = messages.ClusterUpdate(desiredNodeVersion=version)

    try:
      op = client.projects_zones_clusters.Update(
          messages.ContainerProjectsZonesClustersUpdateRequest(
              clusterId=ref.clusterId,
              zone=ref.zone,
              projectId=ref.projectId,
              updateClusterRequest=messages.UpdateClusterRequest(
                  update=update)))
    except apitools_base.HttpError as error:
      raise exceptions.HttpException(util.GetError(error))

    if args.wait:
      util.WaitForOperation(
          op, ref.projectId, self.context,
          'Upgrading {0}'.format(ref.clusterId))

      log.UpdatedResource(ref)
