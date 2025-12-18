# refinerycalc.RateApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_rate_get**](RateApi.md#v1_rate_get) | **GET** /v1/rate | Get Api Rate Limit

# **v1_rate_get**
> RateLimitModel v1_rate_get()

Get Api Rate Limit

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
api_instance = refinerycalc.RateApi(refinerycalc.ApiClient(configuration))

try:
    # Get Api Rate Limit
    api_response = api_instance.v1_rate_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RateApi->v1_rate_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RateLimitModel**](RateLimitModel.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

