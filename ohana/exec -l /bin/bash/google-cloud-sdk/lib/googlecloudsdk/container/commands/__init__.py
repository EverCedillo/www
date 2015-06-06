# Copyright 2014 Google Inc. All Rights Reserved.

"""The main command group for cloud container."""

import argparse
import os

from googlecloudapis.container import v1beta1 as container_v1beta1
from googlecloudapis.container import v1beta2 as container_v1beta2
from googlecloudsdk.calliope import actions
from googlecloudsdk.calliope import base
from googlecloudsdk.calliope import exceptions
from googlecloudsdk.core import properties
from googlecloudsdk.core import resolvers
from googlecloudsdk.core import resources as cloud_resources


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class Container(base.Group):
  """Deploy and manage clusters of machines for running containers."""

  DEFAULT_API_VERSION = 'v1beta1'

  @staticmethod
  def Args(parser):
    """Add arguments to the parser.

    Args:
      parser: argparse.ArgumentParser, This is a standard argparser parser with
        which you can register arguments.  See the public argparse documentation
        for its capabilities.
    """
    parser.add_argument(
        '--api-version', help=argparse.SUPPRESS,
        action=actions.StoreProperty(
            properties.VALUES.api_client_overrides.container))
    parser.add_argument(
        '--zone', '-z',
        help='The compute zone (e.g. us-central1-a) for the cluster',
        action=actions.StoreProperty(properties.VALUES.compute.zone))

  def Filter(self, context, args):
    """Modify the context that will be given to this group's commands when run.

    Args:
      context: {str:object}, A set of key-value pairs that can be used for
          common initialization among commands.
      args: argparse.Namespace: The same namespace given to the corresponding
          .Run() invocation.

    Returns:
      The refined command context.
    """

    api_version = (properties.VALUES.api_client_overrides.container.Get()
                   or self.DEFAULT_API_VERSION)
    endpoint_url = properties.VALUES.api_endpoint_overrides.container.Get()

    if api_version == 'v1beta1':
      api = container_v1beta1
      api_client = api.ContainerV1beta1
      zone_field = 'zoneId'
    elif api_version == 'v1beta2':
      api = container_v1beta2
      api_client = api.ContainerV1beta2
      zone_field = 'zone'
    else:
      raise exceptions.InvalidArgumentException(
          'api_client_overrides/container',
          '{0} is not a valid api version'.format(api_version))

    context['container_client'] = api_client(
        url=endpoint_url,
        get_credentials=False,
        http=self.Http())
    context['container_messages'] = api
    context['registry'] = cloud_resources.REGISTRY.CloneAndSwitchAPIs(
        context['container_client'])
    context['registry'].SetParamDefault(
        api='compute', collection=None, param='project',
        resolver=resolvers.FromProperty(properties.VALUES.core.project))
    context['registry'].SetParamDefault(
        api='container', collection=None, param='projectId',
        resolver=resolvers.FromProperty(properties.VALUES.core.project))
    context['registry'].SetParamDefault(
        api='container', collection=None, param=zone_field,
        resolver=resolvers.FromProperty(properties.VALUES.compute.zone))

    return context
