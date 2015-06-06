"""Generated client library for cloudresourcemanager version v1beta1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from googlecloudapis.apitools.base.py import base_api
from googlecloudapis.cloudresourcemanager.v1beta1 import cloudresourcemanager_v1beta1_messages as messages


class CloudresourcemanagerV1beta1(base_api.BaseApiClient):
  """Generated client library for service cloudresourcemanager version v1beta1."""

  MESSAGES_MODULE = messages

  _PACKAGE = u'cloudresourcemanager'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v1beta1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = ''
  _CLIENT_CLASS_NAME = u'CloudresourcemanagerV1beta1'
  _URL_VERSION = u'v1beta1'

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new cloudresourcemanager handle."""
    url = url or u'https://cloudresourcemanager.googleapis.com/'
    super(CloudresourcemanagerV1beta1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.projects = self.ProjectsService(self)

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(CloudresourcemanagerV1beta1.ProjectsService, self).__init__(client)
      self._method_configs = {
          'Create': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'cloudresourcemanager.projects.create',
              ordered_params=[],
              path_params=[],
              query_params=[],
              relative_path=u'v1beta1/projects',
              request_field='<request>',
              request_type_name=u'Project',
              response_type_name=u'Project',
              supports_download=False,
          ),
          'Delete': base_api.ApiMethodInfo(
              http_method=u'DELETE',
              method_id=u'cloudresourcemanager.projects.delete',
              ordered_params=[u'projectId'],
              path_params=[u'projectId'],
              query_params=[],
              relative_path=u'v1beta1/projects/{projectId}',
              request_field='',
              request_type_name=u'CloudresourcemanagerProjectsDeleteRequest',
              response_type_name=u'Empty',
              supports_download=False,
          ),
          'Get': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'cloudresourcemanager.projects.get',
              ordered_params=[u'projectId'],
              path_params=[u'projectId'],
              query_params=[],
              relative_path=u'v1beta1/projects/{projectId}',
              request_field='',
              request_type_name=u'CloudresourcemanagerProjectsGetRequest',
              response_type_name=u'Project',
              supports_download=False,
          ),
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'cloudresourcemanager.projects.list',
              ordered_params=[],
              path_params=[],
              query_params=[u'filter', u'pageSize', u'pageToken'],
              relative_path=u'v1beta1/projects',
              request_field='',
              request_type_name=u'CloudresourcemanagerProjectsListRequest',
              response_type_name=u'ListProjectsResponse',
              supports_download=False,
          ),
          'Undelete': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'cloudresourcemanager.projects.undelete',
              ordered_params=[u'projectId'],
              path_params=[u'projectId'],
              query_params=[],
              relative_path=u'v1beta1/projects/{projectId}:undelete',
              request_field='',
              request_type_name=u'CloudresourcemanagerProjectsUndeleteRequest',
              response_type_name=u'Empty',
              supports_download=False,
          ),
          'Update': base_api.ApiMethodInfo(
              http_method=u'PUT',
              method_id=u'cloudresourcemanager.projects.update',
              ordered_params=[u'projectId'],
              path_params=[u'projectId'],
              query_params=[],
              relative_path=u'v1beta1/projects/{projectId}',
              request_field='<request>',
              request_type_name=u'Project',
              response_type_name=u'Project',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a project resource.

Initially, the project resource is owned by its creator exclusively.
The creator can later grant permission to others to read or update the
project.

Several APIs are activated automatically for the project, including
Google Cloud Storage.

      Args:
        request: (Project) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Project) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Delete(self, request, global_params=None):
      """Marks the project identified by the specified.
`project_id` (for example, `my-project-123`) for deletion.
This method will only affect the project if it has a lifecycle state of
[ACTIVE][cloudresourcemanager.projects.v1beta2.LifecycleState.ACTIVE]
when this method is called. Otherwise this method does nothing (since all
other states are phases of deletion).

This method changes the project's lifecycle state from
[ACTIVE][cloudresourcemanager.projects.v1beta2.LifecycleState.ACTIVE]
to [DELETE_REQUESTED]
[cloudresourcemanager.projects.v1beta2.LifecycleState.DELETE_REQUESTED].
The deletion starts at an unspecified time,
at which point the lifecycle state changes to [DELETE_IN_PROGRESS]
[cloudresourcemanager.projects.v1beta2.LifecycleState.DELETE_IN_PROGRESS].

Until the deletion completes, you can check the lifecycle state
checked by retrieving the project with [GetProject]
[cloudresourcemanager.projects.v1beta2.Projects.GetProject],
and the project remains visible to [ListProjects]
[cloudresourcemanager.projects.v1beta2.Projects.ListProjects].
However, you cannot update the project.

After the deletion completes, the project is not retrievable by
the  [GetProject]
[cloudresourcemanager.projects.v1beta2.Projects.GetProject] and
[ListProjects]
[cloudresourcemanager.projects.v1beta2.Projects.ListProjects] methods.

The caller must have modify permissions for this project.

      Args:
        request: (CloudresourcemanagerProjectsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Get(self, request, global_params=None):
      """Retrieves the project identified by the specified.
`project_id` (for example, `my-project-123`).

The caller must have read permissions for this project.

      Args:
        request: (CloudresourcemanagerProjectsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Project) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    def List(self, request, global_params=None):
      """Lists projects that are visible to the user and satisfy the.
specified filter. This method returns projects in an unspecified order.
New projects do not necessarily appear at the end of the list.

      Args:
        request: (CloudresourcemanagerProjectsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListProjectsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Undelete(self, request, global_params=None):
      """Restores the project identified by the specified.
`project_id` (for example, `my-project-123`).
You can only use this method for a project that has a lifecycle state of
[DELETE_REQUESTED]
[cloudresourcemanager.projects.v1beta2.LifecycleState.DELETE_REQUESTED].
After deletion starts, as indicated by a lifecycle state of
[DELETE_IN_PROGRESS]
[cloudresourcemanager.projects.v1beta2.LifecycleState.DELETE_IN_PROGRESS],
the project cannot be restored.

The caller must have modify permissions for this project.

      Args:
        request: (CloudresourcemanagerProjectsUndeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Undelete')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Update(self, request, global_params=None):
      """Updates the attributes of the project identified by the specified.
`project_id` (for example, `my-project-123`).

The caller must have modify permissions for this project.

      Args:
        request: (Project) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Project) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)
