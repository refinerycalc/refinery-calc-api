# refinerycalc.HydrogenIGMarketApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_hydrogen_igmarket_countries_get**](HydrogenIGMarketApi.md#v1_hydrogen_igmarket_countries_get) | **GET** /v1/hydrogen/igmarket/countries | Get list of available countries for Hydrogen IG Market pricing
[**v1_hydrogen_igmarket_prices_get**](HydrogenIGMarketApi.md#v1_hydrogen_igmarket_prices_get) | **GET** /v1/hydrogen/igmarket/prices | Get Hydrogen IG Market prices by type with optional country and year filters
[**v1_hydrogen_igmarket_years_get**](HydrogenIGMarketApi.md#v1_hydrogen_igmarket_years_get) | **GET** /v1/hydrogen/igmarket/years | Get list of available years for Hydrogen IG Market pricing

# **v1_hydrogen_igmarket_countries_get**
> list[str] v1_hydrogen_igmarket_countries_get()

Get list of available countries for Hydrogen IG Market pricing

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
api_instance = refinerycalc.HydrogenIGMarketApi(refinerycalc.ApiClient(configuration))

try:
    # Get list of available countries for Hydrogen IG Market pricing
    api_response = api_instance.v1_hydrogen_igmarket_countries_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HydrogenIGMarketApi->v1_hydrogen_igmarket_countries_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_hydrogen_igmarket_prices_get**
> list[HydrogenIGMarketPriceApiResponseModel] v1_hydrogen_igmarket_prices_get(type=type, country=country, year=year, uom=uom)

Get Hydrogen IG Market prices by type with optional country and year filters

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
api_instance = refinerycalc.HydrogenIGMarketApi(refinerycalc.ApiClient(configuration))
type = refinerycalc.HydrogenIGMarketType() # HydrogenIGMarketType | Required: Hydrogen IG Market type (GlobalMerchantH2, GlobalPipelineH2, GlobalOnSiteH2, USLH2, USTTH2) (optional)
country = 'country_example' # str | Optional: Filter by country name (optional)
year = 56 # int | Optional: Filter by year (e.g., 2024, 2025) (optional)
uom = refinerycalc.HydrogenIGMarketPriceUnit() # HydrogenIGMarketPriceUnit | Optional: Unit of measure (Ccf, Kg, Lb, Mscf, Ton). Defaults to Ccf (optional)

try:
    # Get Hydrogen IG Market prices by type with optional country and year filters
    api_response = api_instance.v1_hydrogen_igmarket_prices_get(type=type, country=country, year=year, uom=uom)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HydrogenIGMarketApi->v1_hydrogen_igmarket_prices_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**HydrogenIGMarketType**](.md)| Required: Hydrogen IG Market type (GlobalMerchantH2, GlobalPipelineH2, GlobalOnSiteH2, USLH2, USTTH2) | [optional] 
 **country** | **str**| Optional: Filter by country name | [optional] 
 **year** | **int**| Optional: Filter by year (e.g., 2024, 2025) | [optional] 
 **uom** | [**HydrogenIGMarketPriceUnit**](.md)| Optional: Unit of measure (Ccf, Kg, Lb, Mscf, Ton). Defaults to Ccf | [optional] 

### Return type

[**list[HydrogenIGMarketPriceApiResponseModel]**](HydrogenIGMarketPriceApiResponseModel.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_hydrogen_igmarket_years_get**
> list[int] v1_hydrogen_igmarket_years_get()

Get list of available years for Hydrogen IG Market pricing

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
api_instance = refinerycalc.HydrogenIGMarketApi(refinerycalc.ApiClient(configuration))

try:
    # Get list of available years for Hydrogen IG Market pricing
    api_response = api_instance.v1_hydrogen_igmarket_years_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HydrogenIGMarketApi->v1_hydrogen_igmarket_years_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[int]**

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

