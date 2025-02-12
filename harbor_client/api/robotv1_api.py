"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from harbor_client.api_client import ApiClient, Endpoint as _Endpoint
from harbor_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from harbor_client.model.errors import Errors
from harbor_client.model.robot import Robot
from harbor_client.model.robot_create_v1 import RobotCreateV1
from harbor_client.model.robot_created import RobotCreated


class Robotv1Api(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_robot_v1(
            self,
            project_name_or_id,
            robot_create_v1,
            **kwargs
        ):
            """Create a robot account  # noqa: E501

            Create a robot account  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_robot_v1(project_name_or_id, robot_create_v1, async_req=True)
            >>> result = thread.get()

            Args:
                project_name_or_id (str): The name or id of the project
                robot_create_v1 (RobotCreateV1): The JSON object of a robot account.

            Keyword Args:
                x_request_id (str): An unique ID for the request. [optional]
                x_is_resource_name (bool): The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name.. [optional] if omitted the server will use the default value of False
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                RobotCreated
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['project_name_or_id'] = \
                project_name_or_id
            kwargs['robot_create_v1'] = \
                robot_create_v1
            return self.call_with_http_info(**kwargs)

        self.create_robot_v1 = _Endpoint(
            settings={
                'response_type': (RobotCreated,),
                'auth': [
                    'basic'
                ],
                'endpoint_path': '/projects/{project_name_or_id}/robots',
                'operation_id': 'create_robot_v1',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_name_or_id',
                    'robot_create_v1',
                    'x_request_id',
                    'x_is_resource_name',
                ],
                'required': [
                    'project_name_or_id',
                    'robot_create_v1',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'x_request_id',
                ]
            },
            root_map={
                'validations': {
                    ('x_request_id',): {

                        'min_length': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'project_name_or_id':
                        (str,),
                    'robot_create_v1':
                        (RobotCreateV1,),
                    'x_request_id':
                        (str,),
                    'x_is_resource_name':
                        (bool,),
                },
                'attribute_map': {
                    'project_name_or_id': 'project_name_or_id',
                    'x_request_id': 'X-Request-Id',
                    'x_is_resource_name': 'X-Is-Resource-Name',
                },
                'location_map': {
                    'project_name_or_id': 'path',
                    'robot_create_v1': 'body',
                    'x_request_id': 'header',
                    'x_is_resource_name': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__create_robot_v1
        )

        def __delete_robot_v1(
            self,
            project_name_or_id,
            robot_id,
            **kwargs
        ):
            """Delete a robot account  # noqa: E501

            This endpoint deletes specific robot account information by robot ID.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_robot_v1(project_name_or_id, robot_id, async_req=True)
            >>> result = thread.get()

            Args:
                project_name_or_id (str): The name or id of the project
                robot_id (int): Robot ID

            Keyword Args:
                x_request_id (str): An unique ID for the request. [optional]
                x_is_resource_name (bool): The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name.. [optional] if omitted the server will use the default value of False
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['project_name_or_id'] = \
                project_name_or_id
            kwargs['robot_id'] = \
                robot_id
            return self.call_with_http_info(**kwargs)

        self.delete_robot_v1 = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'basic'
                ],
                'endpoint_path': '/projects/{project_name_or_id}/robots/{robot_id}',
                'operation_id': 'delete_robot_v1',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_name_or_id',
                    'robot_id',
                    'x_request_id',
                    'x_is_resource_name',
                ],
                'required': [
                    'project_name_or_id',
                    'robot_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'x_request_id',
                ]
            },
            root_map={
                'validations': {
                    ('x_request_id',): {

                        'min_length': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'project_name_or_id':
                        (str,),
                    'robot_id':
                        (int,),
                    'x_request_id':
                        (str,),
                    'x_is_resource_name':
                        (bool,),
                },
                'attribute_map': {
                    'project_name_or_id': 'project_name_or_id',
                    'robot_id': 'robot_id',
                    'x_request_id': 'X-Request-Id',
                    'x_is_resource_name': 'X-Is-Resource-Name',
                },
                'location_map': {
                    'project_name_or_id': 'path',
                    'robot_id': 'path',
                    'x_request_id': 'header',
                    'x_is_resource_name': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__delete_robot_v1
        )

        def __get_robot_by_idv1(
            self,
            project_name_or_id,
            robot_id,
            **kwargs
        ):
            """Get a robot account  # noqa: E501

            This endpoint returns specific robot account information by robot ID.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_robot_by_idv1(project_name_or_id, robot_id, async_req=True)
            >>> result = thread.get()

            Args:
                project_name_or_id (str): The name or id of the project
                robot_id (int): Robot ID

            Keyword Args:
                x_request_id (str): An unique ID for the request. [optional]
                x_is_resource_name (bool): The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name.. [optional] if omitted the server will use the default value of False
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Robot
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['project_name_or_id'] = \
                project_name_or_id
            kwargs['robot_id'] = \
                robot_id
            return self.call_with_http_info(**kwargs)

        self.get_robot_by_idv1 = _Endpoint(
            settings={
                'response_type': (Robot,),
                'auth': [
                    'basic'
                ],
                'endpoint_path': '/projects/{project_name_or_id}/robots/{robot_id}',
                'operation_id': 'get_robot_by_idv1',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_name_or_id',
                    'robot_id',
                    'x_request_id',
                    'x_is_resource_name',
                ],
                'required': [
                    'project_name_or_id',
                    'robot_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'x_request_id',
                ]
            },
            root_map={
                'validations': {
                    ('x_request_id',): {

                        'min_length': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'project_name_or_id':
                        (str,),
                    'robot_id':
                        (int,),
                    'x_request_id':
                        (str,),
                    'x_is_resource_name':
                        (bool,),
                },
                'attribute_map': {
                    'project_name_or_id': 'project_name_or_id',
                    'robot_id': 'robot_id',
                    'x_request_id': 'X-Request-Id',
                    'x_is_resource_name': 'X-Is-Resource-Name',
                },
                'location_map': {
                    'project_name_or_id': 'path',
                    'robot_id': 'path',
                    'x_request_id': 'header',
                    'x_is_resource_name': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_robot_by_idv1
        )

        def __list_robot_v1(
            self,
            project_name_or_id,
            **kwargs
        ):
            """Get all robot accounts of specified project  # noqa: E501

            Get all robot accounts of specified project  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_robot_v1(project_name_or_id, async_req=True)
            >>> result = thread.get()

            Args:
                project_name_or_id (str): The name or id of the project

            Keyword Args:
                x_request_id (str): An unique ID for the request. [optional]
                x_is_resource_name (bool): The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name.. [optional] if omitted the server will use the default value of False
                page (int): The page number. [optional] if omitted the server will use the default value of 1
                page_size (int): The size of per page. [optional] if omitted the server will use the default value of 10
                q (str): Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max]. [optional]
                sort (str): Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\". [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                [Robot]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['project_name_or_id'] = \
                project_name_or_id
            return self.call_with_http_info(**kwargs)

        self.list_robot_v1 = _Endpoint(
            settings={
                'response_type': ([Robot],),
                'auth': [
                    'basic'
                ],
                'endpoint_path': '/projects/{project_name_or_id}/robots',
                'operation_id': 'list_robot_v1',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_name_or_id',
                    'x_request_id',
                    'x_is_resource_name',
                    'page',
                    'page_size',
                    'q',
                    'sort',
                ],
                'required': [
                    'project_name_or_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'x_request_id',
                    'page_size',
                ]
            },
            root_map={
                'validations': {
                    ('x_request_id',): {

                        'min_length': 1,
                    },
                    ('page_size',): {

                        'inclusive_maximum': 100,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'project_name_or_id':
                        (str,),
                    'x_request_id':
                        (str,),
                    'x_is_resource_name':
                        (bool,),
                    'page':
                        (int,),
                    'page_size':
                        (int,),
                    'q':
                        (str,),
                    'sort':
                        (str,),
                },
                'attribute_map': {
                    'project_name_or_id': 'project_name_or_id',
                    'x_request_id': 'X-Request-Id',
                    'x_is_resource_name': 'X-Is-Resource-Name',
                    'page': 'page',
                    'page_size': 'page_size',
                    'q': 'q',
                    'sort': 'sort',
                },
                'location_map': {
                    'project_name_or_id': 'path',
                    'x_request_id': 'header',
                    'x_is_resource_name': 'header',
                    'page': 'query',
                    'page_size': 'query',
                    'q': 'query',
                    'sort': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__list_robot_v1
        )

        def __update_robot_v1(
            self,
            project_name_or_id,
            robot_id,
            robot,
            **kwargs
        ):
            """Update status of robot account.  # noqa: E501

            Used to disable/enable a specified robot account.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_robot_v1(project_name_or_id, robot_id, robot, async_req=True)
            >>> result = thread.get()

            Args:
                project_name_or_id (str): The name or id of the project
                robot_id (int): Robot ID
                robot (Robot): The JSON object of a robot account.

            Keyword Args:
                x_request_id (str): An unique ID for the request. [optional]
                x_is_resource_name (bool): The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name.. [optional] if omitted the server will use the default value of False
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['project_name_or_id'] = \
                project_name_or_id
            kwargs['robot_id'] = \
                robot_id
            kwargs['robot'] = \
                robot
            return self.call_with_http_info(**kwargs)

        self.update_robot_v1 = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'basic'
                ],
                'endpoint_path': '/projects/{project_name_or_id}/robots/{robot_id}',
                'operation_id': 'update_robot_v1',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_name_or_id',
                    'robot_id',
                    'robot',
                    'x_request_id',
                    'x_is_resource_name',
                ],
                'required': [
                    'project_name_or_id',
                    'robot_id',
                    'robot',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'x_request_id',
                ]
            },
            root_map={
                'validations': {
                    ('x_request_id',): {

                        'min_length': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'project_name_or_id':
                        (str,),
                    'robot_id':
                        (int,),
                    'robot':
                        (Robot,),
                    'x_request_id':
                        (str,),
                    'x_is_resource_name':
                        (bool,),
                },
                'attribute_map': {
                    'project_name_or_id': 'project_name_or_id',
                    'robot_id': 'robot_id',
                    'x_request_id': 'X-Request-Id',
                    'x_is_resource_name': 'X-Is-Resource-Name',
                },
                'location_map': {
                    'project_name_or_id': 'path',
                    'robot_id': 'path',
                    'robot': 'body',
                    'x_request_id': 'header',
                    'x_is_resource_name': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__update_robot_v1
        )
