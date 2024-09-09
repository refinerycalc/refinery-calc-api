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
from refinerycalc.api.refineries_api import RefineriesApi  # noqa: E501
from refinerycalc.rest import ApiException


class TestRefineriesApi(unittest.TestCase):
    """RefineriesApi unit test stubs"""

    def setUp(self):
        self.api = RefineriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_refineries_aggregates_get(self):
        """Test case for v1_refineries_aggregates_get

        Get Aggregated Refineries by datasource. user can also filter refineries by providing it's name, region and country.  # noqa: E501
        """
        pass

    def test_v1_refineries_get(self):
        """Test case for v1_refineries_get

        Get all Refineries by datasource, user can also filter refineries by providing it's name, region and country.  # noqa: E501
        """
        pass

    def test_v1_refineries_id_crudes_get(self):
        """Test case for v1_refineries_id_crudes_get

        Get list of crudes for a particular refinery.  # noqa: E501
        """
        pass

    def test_v1_refineries_id_get(self):
        """Test case for v1_refineries_id_get

        Get Refinery by Id.  # noqa: E501
        """
        pass

    def test_v1_refineries_id_units_get(self):
        """Test case for v1_refineries_id_units_get

        Get all units of refinery id.  # noqa: E501
        """
        pass

    def test_v1_refineries_individual_get(self):
        """Test case for v1_refineries_individual_get

        Get Individual Refineries by datasource. user can also filter refineries by providing it's name, region and country.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()