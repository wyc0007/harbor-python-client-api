# harbor_client.ImmutableApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_immu_rule**](ImmutableApi.md#create_immu_rule) | **POST** /projects/{project_name_or_id}/immutabletagrules | Add an immutable tag rule to current project
[**delete_immu_rule**](ImmutableApi.md#delete_immu_rule) | **DELETE** /projects/{project_name_or_id}/immutabletagrules/{immutable_rule_id} | Delete the immutable tag rule.
[**list_immu_rules**](ImmutableApi.md#list_immu_rules) | **GET** /projects/{project_name_or_id}/immutabletagrules | List all immutable tag rules of current project
[**update_immu_rule**](ImmutableApi.md#update_immu_rule) | **PUT** /projects/{project_name_or_id}/immutabletagrules/{immutable_rule_id} | Update the immutable tag rule or enable or disable the rule


# **create_immu_rule**
> create_immu_rule(project_name_or_id, immutable_rule)

Add an immutable tag rule to current project

This endpoint add an immutable tag rule to the project 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import immutable_api
from harbor_client.model.immutable_rule import ImmutableRule
from harbor_client.model.errors import Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = harbor_client.Configuration(
    host = "http://localhost/api/v2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = immutable_api.ImmutableApi(api_client)
    project_name_or_id = "project_name_or_id_example" # str | The name or id of the project
    immutable_rule = ImmutableRule(
        id=1,
        priority=1,
        disabled=True,
        action="action_example",
        template="template_example",
        params={
            "key": {},
        },
        tag_selectors=[
            ImmutableSelector(
                kind="kind_example",
                decoration="decoration_example",
                pattern="pattern_example",
                extras="extras_example",
            ),
        ],
        scope_selectors={
            "key": [
                ImmutableSelector(
                    kind="kind_example",
                    decoration="decoration_example",
                    pattern="pattern_example",
                    extras="extras_example",
                ),
            ],
        },
    ) # ImmutableRule | 
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)
    x_is_resource_name = False # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Add an immutable tag rule to current project
        api_instance.create_immu_rule(project_name_or_id, immutable_rule)
    except harbor_client.ApiException as e:
        print("Exception when calling ImmutableApi->create_immu_rule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add an immutable tag rule to current project
        api_instance.create_immu_rule(project_name_or_id, immutable_rule, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
    except harbor_client.ApiException as e:
        print("Exception when calling ImmutableApi->create_immu_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project |
 **immutable_rule** | [**ImmutableRule**](ImmutableRule.md)|  |
 **x_request_id** | **str**| An unique ID for the request | [optional]
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] if omitted the server will use the default value of False

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * X-Request-Id - The ID of the corresponding request for the response <br>  * Location - The URL of the created resource <br>  |
**400** | Bad request |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**404** | Not found |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_immu_rule**
> delete_immu_rule(project_name_or_id, immutable_rule_id)

Delete the immutable tag rule.

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import immutable_api
from harbor_client.model.errors import Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = harbor_client.Configuration(
    host = "http://localhost/api/v2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = immutable_api.ImmutableApi(api_client)
    project_name_or_id = "project_name_or_id_example" # str | The name or id of the project
    immutable_rule_id = 1 # int | The ID of the immutable rule
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)
    x_is_resource_name = False # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete the immutable tag rule.
        api_instance.delete_immu_rule(project_name_or_id, immutable_rule_id)
    except harbor_client.ApiException as e:
        print("Exception when calling ImmutableApi->delete_immu_rule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete the immutable tag rule.
        api_instance.delete_immu_rule(project_name_or_id, immutable_rule_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
    except harbor_client.ApiException as e:
        print("Exception when calling ImmutableApi->delete_immu_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project |
 **immutable_rule_id** | **int**| The ID of the immutable rule |
 **x_request_id** | **str**| An unique ID for the request | [optional]
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] if omitted the server will use the default value of False

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**400** | Bad request |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_immu_rules**
> [ImmutableRule] list_immu_rules(project_name_or_id)

List all immutable tag rules of current project

This endpoint returns the immutable tag rules of a project 

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import immutable_api
from harbor_client.model.immutable_rule import ImmutableRule
from harbor_client.model.errors import Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = harbor_client.Configuration(
    host = "http://localhost/api/v2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = immutable_api.ImmutableApi(api_client)
    project_name_or_id = "project_name_or_id_example" # str | The name or id of the project
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)
    x_is_resource_name = False # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) if omitted the server will use the default value of False
    page = 1 # int | The page number (optional) if omitted the server will use the default value of 1
    page_size = 10 # int | The size of per page (optional) if omitted the server will use the default value of 10
    q = "q_example" # str | Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max] (optional)
    sort = "sort_example" # str | Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \"sort=field1,-field2\" (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all immutable tag rules of current project
        api_response = api_instance.list_immu_rules(project_name_or_id)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ImmutableApi->list_immu_rules: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all immutable tag rules of current project
        api_response = api_instance.list_immu_rules(project_name_or_id, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name, page=page, page_size=page_size, q=q, sort=sort)
        pprint(api_response)
    except harbor_client.ApiException as e:
        print("Exception when calling ImmutableApi->list_immu_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project |
 **x_request_id** | **str**| An unique ID for the request | [optional]
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] if omitted the server will use the default value of False
 **page** | **int**| The page number | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| The size of per page | [optional] if omitted the server will use the default value of 10
 **q** | **str**| Query string to query resources. Supported query patterns are \&quot;exact match(k&#x3D;v)\&quot;, \&quot;fuzzy match(k&#x3D;~v)\&quot;, \&quot;range(k&#x3D;[min~max])\&quot;, \&quot;list with union releationship(k&#x3D;{v1 v2 v3})\&quot; and \&quot;list with intersetion relationship(k&#x3D;(v1 v2 v3))\&quot;. The value of range and list can be string(enclosed by \&quot; or &#39;), integer or time(in format \&quot;2020-04-09 02:36:00\&quot;). All of these query patterns should be put in the query string \&quot;q&#x3D;xxx\&quot; and splitted by \&quot;,\&quot;. e.g. q&#x3D;k1&#x3D;v1,k2&#x3D;~v2,k3&#x3D;[min~max] | [optional]
 **sort** | **str**| Sort the resource list in ascending or descending order. e.g. sort by field1 in ascending orderr and field2 in descending order with \&quot;sort&#x3D;field1,-field2\&quot; | [optional]

### Return type

[**[ImmutableRule]**](ImmutableRule.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * X-Total-Count - The total count of available items <br>  * Link - Link to previous page and next page <br>  |
**400** | Bad request |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_immu_rule**
> update_immu_rule(project_name_or_id, immutable_rule_id, immutable_rule)

Update the immutable tag rule or enable or disable the rule

### Example

* Basic Authentication (basic):
```python
import time
import harbor_client
from harbor_client.api import immutable_api
from harbor_client.model.immutable_rule import ImmutableRule
from harbor_client.model.errors import Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = harbor_client.Configuration(
    host = "http://localhost/api/v2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = harbor_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with harbor_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = immutable_api.ImmutableApi(api_client)
    project_name_or_id = "project_name_or_id_example" # str | The name or id of the project
    immutable_rule_id = 1 # int | The ID of the immutable rule
    immutable_rule = ImmutableRule(
        id=1,
        priority=1,
        disabled=True,
        action="action_example",
        template="template_example",
        params={
            "key": {},
        },
        tag_selectors=[
            ImmutableSelector(
                kind="kind_example",
                decoration="decoration_example",
                pattern="pattern_example",
                extras="extras_example",
            ),
        ],
        scope_selectors={
            "key": [
                ImmutableSelector(
                    kind="kind_example",
                    decoration="decoration_example",
                    pattern="pattern_example",
                    extras="extras_example",
                ),
            ],
        },
    ) # ImmutableRule | 
    x_request_id = "X-Request-Id_example" # str | An unique ID for the request (optional)
    x_is_resource_name = False # bool | The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Update the immutable tag rule or enable or disable the rule
        api_instance.update_immu_rule(project_name_or_id, immutable_rule_id, immutable_rule)
    except harbor_client.ApiException as e:
        print("Exception when calling ImmutableApi->update_immu_rule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the immutable tag rule or enable or disable the rule
        api_instance.update_immu_rule(project_name_or_id, immutable_rule_id, immutable_rule, x_request_id=x_request_id, x_is_resource_name=x_is_resource_name)
    except harbor_client.ApiException as e:
        print("Exception when calling ImmutableApi->update_immu_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name_or_id** | **str**| The name or id of the project |
 **immutable_rule_id** | **int**| The ID of the immutable rule |
 **immutable_rule** | [**ImmutableRule**](ImmutableRule.md)|  |
 **x_request_id** | **str**| An unique ID for the request | [optional]
 **x_is_resource_name** | **bool**| The flag to indicate whether the parameter which supports both name and id in the path is the name of the resource. When the X-Is-Resource-Name is false and the parameter can be converted to an integer, the parameter will be as an id, otherwise, it will be as a name. | [optional] if omitted the server will use the default value of False

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**400** | Bad request |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**401** | Unauthorized |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**403** | Forbidden |  * X-Request-Id - The ID of the corresponding request for the response <br>  |
**500** | Internal server error |  * X-Request-Id - The ID of the corresponding request for the response <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

