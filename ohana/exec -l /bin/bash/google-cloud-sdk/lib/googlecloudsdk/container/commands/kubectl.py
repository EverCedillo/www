# Copyright 2014 Google Inc. All Rights Reserved.

"""Passthrough command for calling kubectl from gcloud."""
import argparse

from googlecloudsdk.calliope import actions
from googlecloudsdk.calliope import base
from googlecloudsdk.calliope import exceptions
from googlecloudsdk.container.lib import util
from googlecloudsdk.core import properties


DEPRECATION_WARNING = '''\
This command is deprecated. Use kubectl directly with the cluster.
{use_context}
kubectl {args}
'''


class Kubectl(base.Command):
  """DEPRECATED pass-through command to call kubectl with arbitrary arguments.

  See https://cloud.google.com/container-engine/docs/kubectl for
  kubectl documentation.
  """

  @staticmethod
  def Args(parser):
    """Register flags for this command.

    Args:
      parser: An argparse.ArgumentParser-like object. It is mocked out in order
          to capture some information, but behaves like an ArgumentParser.
    """
    parser.add_argument(
        '--purge-config-cache',
        help='Clear cached config data for the cluster. If set, will call '
        '\'container clusters describe\' directly to get cluster data before '
        'executing kubernetes client command.',
        action='store_true')
    parser.add_argument(
        '--cluster', '-n',
        help='The name of the cluster to issue commands to.',
        action=actions.StoreProperty(properties.VALUES.container.cluster))
    parser.add_argument(
        'kubectl_args',
        nargs=argparse.REMAINDER,
        help='Arbitrary arguments to pass to kubectl')

  @exceptions.RaiseToolExceptionInsteadOf(util.Error)
  def Run(self, args):
    """This is what gets called when the user runs this command.

    Args:
      args: an argparse namespace. All the arguments that were provided to this
        command invocation.

    Raises:
      util.Error: command is deprecated
    """
    raise util.Error(DEPRECATION_WARNING.format(
        use_context='\ngcloud alpha container get-credentials',
        args=' '.join(args.kubectl_args)))

Kubectl.detailed_help = {
    'brief': 'Call kubectl with arbitrary arguments.',
    'DESCRIPTION': """\
        This command is deprecated! You can run kubectl directly after calling

        $ gcloud alpha container get-credentials
        $ kubectl ...

        """.format(
            context=util.ClusterConfig.KUBECONTEXT_FORMAT.format(
                project='PROJECT', zone='ZONE', cluster='CLUSTER'))
}

