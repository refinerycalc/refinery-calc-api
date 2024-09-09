# coding: utf-8

"""
    Refinery Calc API Documentation

    Integrate the powerful Refinery Calc Engine into your process using this API.  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: support@refinerycalc.com.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from refinerycalc.api_client import ApiClient


class WeatherForecastApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_weather_forecast(self, **kwargs):  # noqa: E501
        """get_weather_forecast  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_weather_forecast(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version:
        :param str accept_version:
        :return: list[WeatherForecast]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_weather_forecast_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_weather_forecast_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_weather_forecast_with_http_info(self, **kwargs):  # noqa: E501
        """get_weather_forecast  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_weather_forecast_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version:
        :param str accept_version:
        :return: list[WeatherForecast]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_version', 'accept_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_weather_forecast" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'api_version' in params:
            query_params.append(('api-version', params['api_version']))  # noqa: E501

        header_params = {}
        if 'accept_version' in params:
            header_params['Accept-Version'] = params['accept_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain; api-version=1.0', 'application/json; api-version=1.0', 'text/json; api-version=1.0'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/weatherforecast', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[WeatherForecast]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)