# refinerycalc.WeatherForecastApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_weather_forecast**](WeatherForecastApi.md#get_weather_forecast) | **GET** /weatherforecast | 

# **get_weather_forecast**
> list[WeatherForecast] get_weather_forecast(api_version=api_version, accept_version=accept_version)



### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.WeatherForecastApi()
api_version = 'api_version_example' # str |  (optional)
accept_version = 'accept_version_example' # str |  (optional)

try:
    api_response = api_instance.get_weather_forecast(api_version=api_version, accept_version=accept_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WeatherForecastApi->get_weather_forecast: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | [optional] 
 **accept_version** | **str**|  | [optional] 

### Return type

[**list[WeatherForecast]**](WeatherForecast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain; api-version=1.0, application/json; api-version=1.0, text/json; api-version=1.0

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

