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
from refinerycalc.api.simulations_api import SimulationsApi  # noqa: E501
from refinerycalc.rest import ApiException


class TestSimulationsApi(unittest.TestCase):
    """SimulationsApi unit test stubs"""

    def setUp(self):
        self.api = SimulationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_simulations_get(self):
        """Test case for v1_simulations_get

        Returns simulation list  # noqa: E501
        """
        pass

    def test_v1_simulations_id_delete(self):
        """Test case for v1_simulations_id_delete

        Delete a simulation  # noqa: E501
        """
        pass

    def test_v1_simulations_id_get(self):
        """Test case for v1_simulations_id_get

        Returns simulations refineries details  # noqa: E501
        """
        pass

    def test_v1_simulations_id_output_get(self):
        """Test case for v1_simulations_id_output_get

        Retrieves a OutputModel for the given input simuation Id.  # noqa: E501
        """
        pass

    def test_v1_simulations_id_refineries_advanced_options_patch(self):
        """Test case for v1_simulations_id_refineries_advanced_options_patch

        Updates the advanced options for the given refineries  # noqa: E501
        """
        pass

    def test_v1_simulations_id_refineries_crude_allocation_patch(self):
        """Test case for v1_simulations_id_refineries_crude_allocation_patch

        Update Crude Allocation Value for One or More Refineries  # noqa: E501
        """
        pass

    def test_v1_simulations_id_refineries_crude_allocations_default_patch(self):
        """Test case for v1_simulations_id_refineries_crude_allocations_default_patch

        Refinery set default value for crude compositions  # noqa: E501
        """
        pass

    def test_v1_simulations_id_refineries_crude_prices_default_patch(self):
        """Test case for v1_simulations_id_refineries_crude_prices_default_patch

        Refinery set default value for crude price  # noqa: E501
        """
        pass

    def test_v1_simulations_id_refineries_crude_prices_patch(self):
        """Test case for v1_simulations_id_refineries_crude_prices_patch

        Update Crude Prices for One or More Refineries  # noqa: E501
        """
        pass

    def test_v1_simulations_id_refineries_crudes_patch(self):
        """Test case for v1_simulations_id_refineries_crudes_patch

        Update Crudes for One or More Refineries  # noqa: E501
        """
        pass

    def test_v1_simulations_id_refineries_endpoint_mode_patch(self):
        """Test case for v1_simulations_id_refineries_endpoint_mode_patch

        Returns Success or failed  # noqa: E501
        """
        pass

    def test_v1_simulations_id_refineries_endpoints_default_patch(self):
        """Test case for v1_simulations_id_refineries_endpoints_default_patch

        Refinery set default value for end points  # noqa: E501
        """
        pass

    def test_v1_simulations_id_refineries_get(self):
        """Test case for v1_simulations_id_refineries_get

        Retrieves a list of refineries for the given simulation.  # noqa: E501
        """
        pass

    def test_v1_simulations_id_refineries_intermediate_products_patch(self):
        """Test case for v1_simulations_id_refineries_intermediate_products_patch

        """
        pass

    def test_v1_simulations_id_refineries_post(self):
        """Test case for v1_simulations_id_refineries_post

        Adds a list of refineries to an existing simulation.  # noqa: E501
        """
        pass

    def test_v1_simulations_id_refineries_product_prices_default_patch(self):
        """Test case for v1_simulations_id_refineries_product_prices_default_patch

        Refinery set default value for product prices  # noqa: E501
        """
        pass

    def test_v1_simulations_id_refineries_product_prices_patch(self):
        """Test case for v1_simulations_id_refineries_product_prices_patch

        Simulation's refineries set product price  # noqa: E501
        """
        pass

    def test_v1_simulations_id_refineries_refinery_id_crude_get(self):
        """Test case for v1_simulations_id_refineries_refinery_id_crude_get

        """
        pass

    def test_v1_simulations_id_refineries_refinery_id_delete(self):
        """Test case for v1_simulations_id_refineries_refinery_id_delete

        Remove Refinery from an existing simulation.  # noqa: E501
        """
        pass

    def test_v1_simulations_id_refineries_refinery_id_endpoints_get(self):
        """Test case for v1_simulations_id_refineries_refinery_id_endpoints_get

        Retrieves a list of Endpoints for the given input simuation Id and Refinery Id.  # noqa: E501
        """
        pass

    def test_v1_simulations_id_refineries_refinery_id_product_prices_get(self):
        """Test case for v1_simulations_id_refineries_refinery_id_product_prices_get

        Get product prices for a given simulation  # noqa: E501
        """
        pass

    def test_v1_simulations_id_refineries_refinery_id_units_get(self):
        """Test case for v1_simulations_id_refineries_refinery_id_units_get

        Retrieves Units for a given Simulation and Refinery  # noqa: E501
        """
        pass

    def test_v1_simulations_id_refineries_units_bias_patch(self):
        """Test case for v1_simulations_id_refineries_units_bias_patch

        Update simulation refinery unit bios  # noqa: E501
        """
        pass

    def test_v1_simulations_id_refineries_units_default_patch(self):
        """Test case for v1_simulations_id_refineries_units_default_patch

        Refinery set default value for units  # noqa: E501
        """
        pass

    def test_v1_simulations_id_refineries_units_health_state_patch(self):
        """Test case for v1_simulations_id_refineries_units_health_state_patch

        Update the health state of the specified units for the specified refineries in the given simulation  # noqa: E501
        """
        pass

    def test_v1_simulations_id_refineries_units_mode_patch(self):
        """Test case for v1_simulations_id_refineries_units_mode_patch

        Update simulation refinery unit mode  # noqa: E501
        """
        pass

    def test_v1_simulations_id_refineries_units_rate_patch(self):
        """Test case for v1_simulations_id_refineries_units_rate_patch

        Update simulation refinery unit rate  # noqa: E501
        """
        pass

    def test_v1_simulations_id_refineries_units_toggle_shutdown_status_patch(self):
        """Test case for v1_simulations_id_refineries_units_toggle_shutdown_status_patch

        Update simulation refinery toggle unit status  # noqa: E501
        """
        pass

    def test_v1_simulations_id_refinery_change_endpoint_post(self):
        """Test case for v1_simulations_id_refinery_change_endpoint_post

        Returns Success or failed  # noqa: E501
        """
        pass

    def test_v1_simulations_id_rename_patch(self):
        """Test case for v1_simulations_id_rename_patch

        Rename an existing simulation  # noqa: E501
        """
        pass

    def test_v1_simulations_id_run_post(self):
        """Test case for v1_simulations_id_run_post

        Run a simulation by Id  # noqa: E501
        """
        pass

    def test_v1_simulations_id_run_status_get(self):
        """Test case for v1_simulations_id_run_status_get

        Get simulation run status  # noqa: E501
        """
        pass

    def test_v1_simulations_id_schedule_delete(self):
        """Test case for v1_simulations_id_schedule_delete

        Delete a simulation schedule.  # noqa: E501
        """
        pass

    def test_v1_simulations_id_schedule_post(self):
        """Test case for v1_simulations_id_schedule_post

        Schedule a simulation to run  # noqa: E501
        """
        pass

    def test_v1_simulations_post(self):
        """Test case for v1_simulations_post

        Create a new simulation from a given list of refineries  # noqa: E501
        """
        pass

    def test_v1_simulations_schedules_get(self):
        """Test case for v1_simulations_schedules_get

        Retrieves list of the scheduled simulations.  # noqa: E501
        """
        pass

    def test_v1_simulations_simulation_id_refineries_kero_mode_patch(self):
        """Test case for v1_simulations_simulation_id_refineries_kero_mode_patch

        Update refinery kero mode  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
