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

class RateLimitModel(object):
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
        'rate': 'int',
        'frequency': 'str',
        'usage': 'int'
    }

    attribute_map = {
        'rate': 'rate',
        'frequency': 'frequency',
        'usage': 'usage'
    }

    def __init__(self, rate=None, frequency=None, usage=None):  # noqa: E501
        """RateLimitModel - a model defined in Swagger"""  # noqa: E501
        self._rate = None
        self._frequency = None
        self._usage = None
        self.discriminator = None
        if rate is not None:
            self.rate = rate
        if frequency is not None:
            self.frequency = frequency
        if usage is not None:
            self.usage = usage

    @property
    def rate(self):
        """Gets the rate of this RateLimitModel.  # noqa: E501


        :return: The rate of this RateLimitModel.  # noqa: E501
        :rtype: int
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this RateLimitModel.


        :param rate: The rate of this RateLimitModel.  # noqa: E501
        :type: int
        """

        self._rate = rate

    @property
    def frequency(self):
        """Gets the frequency of this RateLimitModel.  # noqa: E501


        :return: The frequency of this RateLimitModel.  # noqa: E501
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this RateLimitModel.


        :param frequency: The frequency of this RateLimitModel.  # noqa: E501
        :type: str
        """

        self._frequency = frequency

    @property
    def usage(self):
        """Gets the usage of this RateLimitModel.  # noqa: E501


        :return: The usage of this RateLimitModel.  # noqa: E501
        :rtype: int
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this RateLimitModel.


        :param usage: The usage of this RateLimitModel.  # noqa: E501
        :type: int
        """

        self._usage = usage

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
        if issubclass(RateLimitModel, dict):
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
        if not isinstance(other, RateLimitModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
