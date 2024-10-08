# coding: utf-8

"""
    Refinery Calc API Documentation

    Integrate the powerful Refinery Calc Engine into your process using this API.  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: support@refinerycalc.com.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import refinerycalc
from refinerycalc.api.regions_api import RegionsApi  # noqa: E501
from refinerycalc.rest import ApiException


class TestRegionsApi(unittest.TestCase):
    """RegionsApi unit test stubs"""

    def setUp(self):
        self.api = RegionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_regions_get(self):
        """Test case for v1_regions_get

        Get all regions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
