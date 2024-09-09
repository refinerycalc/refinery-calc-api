# refinerycalc.CrudesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_crudes_get**](CrudesApi.md#v1_crudes_get) | **GET** /v1/crudes | Get all crudes

# **v1_crudes_get**
> list[CrudeModel] v1_crudes_get()

Get all crudes

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.CrudesApi()

try:
    # Get all crudes
    api_response = api_instance.v1_crudes_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrudesApi->v1_crudes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CrudeModel]**](CrudeModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

