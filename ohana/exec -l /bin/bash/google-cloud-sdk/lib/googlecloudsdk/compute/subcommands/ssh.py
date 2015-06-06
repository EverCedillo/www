# Copyright 2014 Google Inc. All Rights Reserved.

"""Implements the command for SSHing into an instance."""
import getpass
import re

from googlecloudsdk.calliope import base
from googlecloudsdk.calliope import exceptions
from googlecloudsdk.compute.lib import gaia_utils
from googlecloudsdk.compute.lib import ssh_utils
from googlecloudsdk.compute.lib import utils


def _Args(parser, cli_generator):
  """Argument parsing for ssh, including hook for remote completion."""
  ssh_utils.BaseSSHCLICommand.Args(parser)

  parser.add_argument(
      '--command',
      help='A command to run on the virtual machine.')

  ssh_flags = parser.add_argument(
      '--ssh-flag',
      action='append',
      help='Additional flags to be passed to ssh.')
  ssh_flags.detailed_help = """\
      Additional flags to be passed to *ssh(1)*. It is recommended that flags
      be passed using an assignment operator and quotes. This flag will
      replace occurences of ``%USER%'' and ``%INSTANCE%'' with their
      dereferenced values. Example:

        $ {command} example-instance --zone us-central1-a --ssh-flag="-vvv" --ssh-flag="-L 80:%INSTANCE%:80"

      is equivalent to passing the flags ``--vvv'' and ``-L
      80:162.222.181.197:80'' to *ssh(1)* if the external IP address of
      'example-instance' is 162.222.181.197.
      """

  parser.add_argument(
      '--container',
      help="""\
          The name of a container inside of the virtual machine instance to
          connect to. This only applies to virtual machines that are using
          a Google container virtual machine image. For more information,
          see link:https://developers.google.com/compute/docs/containers[].
          """)

  user_host = parser.add_argument(
      'user_host',
      help='Specifies the instance to SSH into.',
      metavar='[USER@]INSTANCE')
  user_host.completer = utils.GetCompleterForResource('compute.instances',
                                                      cli_generator)
  user_host.detailed_help = """\
      Specifies the instance to SSH into.

      ``USER'' specifies the username with which to SSH. If omitted,
      $USER from the environment is selected.
      """

  implementation_args = parser.add_argument(
      'implementation_args',
      nargs='*',
      help="""\
          Flags and positionals passed to the underlying ssh implementation.
          """,
      metavar='-- IMPLEMENTATION-ARGS')
  implementation_args.detailed_help = """\
      Flags and positionals passed to the underlying ssh implementation.

      The '--' argument must be specified between gcloud specific args on
      the left and IMPLEMENTATION-ARGS on the right. Example:

        $ {command} example-instance --zone us-central1-a -- -vvv -L 80:%INSTANCE%:80
      """

  utils.AddZoneFlag(
      parser,
      resource_type='instance',
      operation_type='connect to',
      cli=cli_generator)


@base.ReleaseTracks(base.ReleaseTrack.GA)
class SshGA(ssh_utils.BaseSSHCLICommand):
  """SSH into a virtual machine instance."""

  def __init__(self, *args, **kwargs):
    super(SshGA, self).__init__(*args, **kwargs)
    self._use_accounts_service = False

  @staticmethod
  def Args(parser):
    cli_generator = SshGA.GetCLIGenerator()
    _Args(parser, cli_generator)

  def Run(self, args):
    super(SshGA, self).Run(args)

    parts = args.user_host.split('@')
    if len(parts) == 1:
      if self._use_accounts_service:  # Using Account Service.
        user = gaia_utils.GetDefaultAccountName(self.http)
      else:  # Uploading keys through metadata.
        user = getpass.getuser()
      instance = parts[0]
    elif len(parts) == 2:
      user, instance = parts
    else:
      raise exceptions.ToolException(
          'Expected argument of the form [USER@]INSTANCE; received [{0}].'
          .format(args.user_host))

    instance_ref = self.CreateZonalReference(instance, args.zone)
    external_ip_address = self.GetInstanceExternalIpAddress(instance_ref)

    ssh_args = [self.ssh_executable]
    if not args.plain:
      ssh_args.extend(self.GetDefaultFlags())
      # Allocates a tty if no command was provided and a container was provided.
      if args.container and not args.command:
        ssh_args.append('-t')

    if args.ssh_flag:
      for flag in args.ssh_flag:
        dereferenced_flag = (
            flag.replace('%USER%', user)
            .replace('%INSTANCE%', external_ip_address))
        ssh_args.append(dereferenced_flag)

    ssh_args.append(ssh_utils.UserHost(user, external_ip_address))

    interactive_ssh = False
    if args.implementation_args:
      # Backslash-escape shell special characters -- ultra conservative.
      pattern = re.compile(r'(\W)')
      ssh_args.append(' '.join(pattern.sub(r'\\\1', arg)
                               for arg in args.implementation_args))
    if args.container:
      ssh_args.append('--')
      ssh_args.append('container_exec')
      ssh_args.append(args.container)
      # Runs the given command inside the given container if --command was
      # specified, otherwise runs /bin/sh.
      if args.command:
        ssh_args.append(args.command)
      else:
        ssh_args.append('/bin/sh')

    elif args.command:
      ssh_args.append('--')
      ssh_args.append(args.command)

    else:
      interactive_ssh = True

    self.ActuallyRun(args, ssh_args, user, external_ip_address,
                     interactive_ssh=interactive_ssh,
                     use_account_service=self._use_accounts_service)


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class SshAlpha(SshGA):
  """SSH into a virtual machine instance."""

  def __init__(self, *args, **kwargs):
    super(SshAlpha, self).__init__(*args, **kwargs)
    self._use_accounts_service = True

  @staticmethod
  def Args(parser):
    cli_generator = SshAlpha.GetCLIGenerator()
    _Args(parser, cli_generator)


def DetailedHelp(version):
  """Construct help text based on the command release track."""
  detailed_help = {
      'brief': 'SSH into a virtual machine instance',
      'DESCRIPTION': """\
        *{command}* is a thin wrapper around the *ssh(1)* command that
        takes care of authentication and the translation of the
        instance name into an IP address.

        This command ensures that the user's public SSH key is present
        in the project's metadata. If the user does not have a public
        SSH key, one is generated using *ssh-keygen(1)*.
        """,
      'EXAMPLES': """\
        To SSH into 'example-instance' in zone ``us-central1-a'', run:

          $ {command} example-instance --zone us-central1-a

        You can also run a command on the virtual machine. For
        example, to get a snapshot of the guest's process tree, run:

          $ {command} example-instance --zone us-central1-a --command "ps -ejH"

        If you are using the Google container virtual machine image, you
        can SSH into one of your containers with:

          $ {command} example-instance --zone us-central1-a --container CONTAINER
        """,
  }
  if version == 'ALPHA':
    detailed_help['DESCRIPTION'] = """\
        *{command}* is a thin wrapper around the *ssh(1)* command that
        takes care of authentication and the translation of the
        instance name into an IP address.

        This command uses the Compute Accounts API to ensure that the user's
        public SSH key is availibe to the VM. This form of key management
        will only work with VMs configured to work with the Compute Accounts
        API. If the user does not have a public SSH key, one is generated using
        *ssh-keygen(1)*.
        """
  return detailed_help

SshGA.detailed_help = DetailedHelp('GA')
SshAlpha.detailed_help = DetailedHelp('ALPHA')
