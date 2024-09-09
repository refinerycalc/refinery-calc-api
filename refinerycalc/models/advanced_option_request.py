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

class AdvancedOptionRequest(object):
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
        'option_type': 'AdvancedOptionType',
        'value': 'float'
    }

    attribute_map = {
        'option_type': 'optionType',
        'value': 'value'
    }

    def __init__(self, option_type=None, value=None):  # noqa: E501
        """AdvancedOptionRequest - a model defined in Swagger"""  # noqa: E501
        self._option_type = None
        self._value = None
        self.discriminator = None
        self.option_type = option_type
        self.value = value

    @property
    def option_type(self):
        """Gets the option_type of this AdvancedOptionRequest.  # noqa: E501


        :return: The option_type of this AdvancedOptionRequest.  # noqa: E501
        :rtype: AdvancedOptionType
        """
        return self._option_type

    @option_type.setter
    def option_type(self, option_type):
        """Sets the option_type of this AdvancedOptionRequest.


        :param option_type: The option_type of this AdvancedOptionRequest.  # noqa: E501
        :type: AdvancedOptionType
        """
        if option_type is None:
            raise ValueError("Invalid value for `option_type`, must not be `None`")  # noqa: E501

        self._option_type = option_type

    @property
    def value(self):
        """Gets the value of this AdvancedOptionRequest.  # noqa: E501


        :return: The value of this AdvancedOptionRequest.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this AdvancedOptionRequest.


        :param value: The value of this AdvancedOptionRequest.  # noqa: E501
        :type: float
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if issubclass(AdvancedOptionRequest, dict):
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
        if not isinstance(other, AdvancedOptionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
