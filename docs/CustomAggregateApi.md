# refinerycalc.CustomAggregateApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_custom_aggregate_create_post**](CustomAggregateApi.md#v1_custom_aggregate_create_post) | **POST** /v1/custom-aggregate/create | Create new Custom Aggregate.
[**v1_custom_aggregate_get**](CustomAggregateApi.md#v1_custom_aggregate_get) | **GET** /v1/custom-aggregate | Get all Custom Aggregates. Optional filtering by name or pricing region.
[**v1_custom_aggregate_id_delete_delete**](CustomAggregateApi.md#v1_custom_aggregate_id_delete_delete) | **DELETE** /v1/custom-aggregate/{id}/delete | Delete Custom Aggregate.
[**v1_custom_aggregate_id_update_patch**](CustomAggregateApi.md#v1_custom_aggregate_id_update_patch) | **PATCH** /v1/custom-aggregate/{id}/update | Update existing Custom Aggregate.

# **v1_custom_aggregate_create_post**
> ApiResponse v1_custom_aggregate_create_post(body=body)

Create new Custom Aggregate.

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
configuration = refinerycalc.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = refinerycalc.CustomAggregateApi(refinerycalc.ApiClient(configuration))
body = refinerycalc.CustomAggregateAddEditRequestModel() # CustomAggregateAddEditRequestModel |  (optional)

try:
    # Create new Custom Aggregate.
    api_response = api_instance.v1_custom_aggregate_create_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomAggregateApi->v1_custom_aggregate_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomAggregateAddEditRequestModel**](CustomAggregateAddEditRequestModel.md)|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_custom_aggregate_get**
> list[CustomAggregateDetailModel] v1_custom_aggregate_get()

Get all Custom Aggregates. Optional filtering by name or pricing region.

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
configuration = refinerycalc.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = refinerycalc.CustomAggregateApi(refinerycalc.ApiClient(configuration))

try:
    # Get all Custom Aggregates. Optional filtering by name or pricing region.
    api_response = api_instance.v1_custom_aggregate_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomAggregateApi->v1_custom_aggregate_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CustomAggregateDetailModel]**](CustomAggregateDetailModel.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_custom_aggregate_id_delete_delete**
> ApiResponse v1_custom_aggregate_id_delete_delete(id)

Delete Custom Aggregate.

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
configuration = refinerycalc.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = refinerycalc.CustomAggregateApi(refinerycalc.ApiClient(configuration))
id = 56 # int | 

try:
    # Delete Custom Aggregate.
    api_response = api_instance.v1_custom_aggregate_id_delete_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomAggregateApi->v1_custom_aggregate_id_delete_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_custom_aggregate_id_update_patch**
> ApiResponse v1_custom_aggregate_id_update_patch(id, body=body)

Update existing Custom Aggregate.

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
configuration = refinerycalc.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = refinerycalc.CustomAggregateApi(refinerycalc.ApiClient(configuration))
id = 56 # int | 
body = refinerycalc.CustomAggregateAddEditRequestModel() # CustomAggregateAddEditRequestModel |  (optional)

try:
    # Update existing Custom Aggregate.
    api_response = api_instance.v1_custom_aggregate_id_update_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomAggregateApi->v1_custom_aggregate_id_update_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**CustomAggregateAddEditRequestModel**](CustomAggregateAddEditRequestModel.md)|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

