# coding: utf-8

"""
    Refinery Calc API Documentation

    Integrate the powerful Refinery Calc Engine into your process using this API.  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: support@refinerycalc.com.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class GetSimulationRequestModel(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'page_number': 'int',
        'page_size': 'int',
        'sort_order': 'SortOrder',
        'sort_by': 'SortBy'
    }

    attribute_map = {
        'page_number': 'pageNumber',
        'page_size': 'pageSize',
        'sort_order': 'sortOrder',
        'sort_by': 'sortBy'
    }

    def __init__(self, page_number=None, page_size=None, sort_order=None, sort_by=None):  # noqa: E501
        """GetSimulationRequestModel - a model defined in Swagger"""  # noqa: E501
        self._page_number = None
        self._page_size = None
        self._sort_order = None
        self._sort_by = None
        self.discriminator = None
        self.page_number = page_number
        self.page_size = page_size
        if sort_order is not None:
            self.sort_order = sort_order
        if sort_by is not None:
            self.sort_by = sort_by

    @property
    def page_number(self):
        """Gets the page_number of this GetSimulationRequestModel.  # noqa: E501


        :return: The page_number of this GetSimulationRequestModel.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this GetSimulationRequestModel.


        :param page_number: The page_number of this GetSimulationRequestModel.  # noqa: E501
        :type: int
        """
        if page_number is None:
            raise ValueError("Invalid value for `page_number`, must not be `None`")  # noqa: E501

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this GetSimulationRequestModel.  # noqa: E501


        :return: The page_size of this GetSimulationRequestModel.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this GetSimulationRequestModel.


        :param page_size: The page_size of this GetSimulationRequestModel.  # noqa: E501
        :type: int
        """
        if page_size is None:
            raise ValueError("Invalid value for `page_size`, must not be `None`")  # noqa: E501

        self._page_size = page_size

    @property
    def sort_order(self):
        """Gets the sort_order of this GetSimulationRequestModel.  # noqa: E501


        :return: The sort_order of this GetSimulationRequestModel.  # noqa: E501
        :rtype: SortOrder
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this GetSimulationRequestModel.


        :param sort_order: The sort_order of this GetSimulationRequestModel.  # noqa: E501
        :type: SortOrder
        """

        self._sort_order = sort_order

    @property
    def sort_by(self):
        """Gets the sort_by of this GetSimulationRequestModel.  # noqa: E501


        :return: The sort_by of this GetSimulationRequestModel.  # noqa: E501
        :rtype: SortBy
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """Sets the sort_by of this GetSimulationRequestModel.


        :param sort_by: The sort_by of this GetSimulationRequestModel.  # noqa: E501
        :type: SortBy
        """

        self._sort_by = sort_by

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GetSimulationRequestModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetSimulationRequestModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
