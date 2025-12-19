# refinerycalc.EndPointsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_endpoints_get**](EndPointsApi.md#v1_endpoints_get) | **GET** /v1/endpoints | Returns end point list
[**v1_endpoints_id_get**](EndPointsApi.md#v1_endpoints_id_get) | **GET** /v1/endpoints/{id} | Get end point by id

# **v1_endpoints_get**
> list[EndPointModel] v1_endpoints_get()

Returns end point list

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
api_instance = refinerycalc.EndPointsApi(refinerycalc.ApiClient(configuration))

try:
    # Returns end point list
    api_response = api_instance.v1_endpoints_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndPointsApi->v1_endpoints_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EndPointModel]**](EndPointModel.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_endpoints_id_get**
> EndPointModel v1_endpoints_id_get(id)

Get end point by id

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
api_instance = refinerycalc.EndPointsApi(refinerycalc.ApiClient(configuration))
id = 56 # int | End point id

try:
    # Get end point by id
    api_response = api_instance.v1_endpoints_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndPointsApi->v1_endpoints_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| End point id | 

### Return type

[**EndPointModel**](EndPointModel.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

