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

class CrudePriceModeCrude(object):
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
        'crude_name': 'str',
        'crude_gpw': 'float',
        'deltas': 'float',
        'flat_price_valuation': 'float',
        'crude_country': 'str'
    }

    attribute_map = {
        'crude_name': 'crudeName',
        'crude_gpw': 'crudeGPW',
        'deltas': 'deltas',
        'flat_price_valuation': 'flatPriceValuation',
        'crude_country': 'crudeCountry'
    }

    def __init__(self, crude_name=None, crude_gpw=None, deltas=None, flat_price_valuation=None, crude_country=None):  # noqa: E501
        """CrudePriceModeCrude - a model defined in Swagger"""  # noqa: E501
        self._crude_name = None
        self._crude_gpw = None
        self._deltas = None
        self._flat_price_valuation = None
        self._crude_country = None
        self.discriminator = None
        if crude_name is not None:
            self.crude_name = crude_name
        if crude_gpw is not None:
            self.crude_gpw = crude_gpw
        if deltas is not None:
            self.deltas = deltas
        if flat_price_valuation is not None:
            self.flat_price_valuation = flat_price_valuation
        if crude_country is not None:
            self.crude_country = crude_country

    @property
    def crude_name(self):
        """Gets the crude_name of this CrudePriceModeCrude.  # noqa: E501


        :return: The crude_name of this CrudePriceModeCrude.  # noqa: E501
        :rtype: str
        """
        return self._crude_name

    @crude_name.setter
    def crude_name(self, crude_name):
        """Sets the crude_name of this CrudePriceModeCrude.


        :param crude_name: The crude_name of this CrudePriceModeCrude.  # noqa: E501
        :type: str
        """

        self._crude_name = crude_name

    @property
    def crude_gpw(self):
        """Gets the crude_gpw of this CrudePriceModeCrude.  # noqa: E501


        :return: The crude_gpw of this CrudePriceModeCrude.  # noqa: E501
        :rtype: float
        """
        return self._crude_gpw

    @crude_gpw.setter
    def crude_gpw(self, crude_gpw):
        """Sets the crude_gpw of this CrudePriceModeCrude.


        :param crude_gpw: The crude_gpw of this CrudePriceModeCrude.  # noqa: E501
        :type: float
        """

        self._crude_gpw = crude_gpw

    @property
    def deltas(self):
        """Gets the deltas of this CrudePriceModeCrude.  # noqa: E501


        :return: The deltas of this CrudePriceModeCrude.  # noqa: E501
        :rtype: float
        """
        return self._deltas

    @deltas.setter
    def deltas(self, deltas):
        """Sets the deltas of this CrudePriceModeCrude.


        :param deltas: The deltas of this CrudePriceModeCrude.  # noqa: E501
        :type: float
        """

        self._deltas = deltas

    @property
    def flat_price_valuation(self):
        """Gets the flat_price_valuation of this CrudePriceModeCrude.  # noqa: E501


        :return: The flat_price_valuation of this CrudePriceModeCrude.  # noqa: E501
        :rtype: float
        """
        return self._flat_price_valuation

    @flat_price_valuation.setter
    def flat_price_valuation(self, flat_price_valuation):
        """Sets the flat_price_valuation of this CrudePriceModeCrude.


        :param flat_price_valuation: The flat_price_valuation of this CrudePriceModeCrude.  # noqa: E501
        :type: float
        """

        self._flat_price_valuation = flat_price_valuation

    @property
    def crude_country(self):
        """Gets the crude_country of this CrudePriceModeCrude.  # noqa: E501


        :return: The crude_country of this CrudePriceModeCrude.  # noqa: E501
        :rtype: str
        """
        return self._crude_country

    @crude_country.setter
    def crude_country(self, crude_country):
        """Sets the crude_country of this CrudePriceModeCrude.


        :param crude_country: The crude_country of this CrudePriceModeCrude.  # noqa: E501
        :type: str
        """

        self._crude_country = crude_country

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
        if issubclass(CrudePriceModeCrude, dict):
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
        if not isinstance(other, CrudePriceModeCrude):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
