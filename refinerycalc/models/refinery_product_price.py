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

class RefineryProductPrice(object):
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
        'uom': 'ProductPriceUomType',
        'refinery_id': 'int',
        'apply_all': 'bool',
        'products': 'list[RefineryProductPriceItem]'
    }

    attribute_map = {
        'uom': 'uom',
        'refinery_id': 'refineryId',
        'apply_all': 'applyAll',
        'products': 'products'
    }

    def __init__(self, uom=None, refinery_id=None, apply_all=None, products=None):  # noqa: E501
        """RefineryProductPrice - a model defined in Swagger"""  # noqa: E501
        self._uom = None
        self._refinery_id = None
        self._apply_all = None
        self._products = None
        self.discriminator = None
        if uom is not None:
            self.uom = uom
        if refinery_id is not None:
            self.refinery_id = refinery_id
        if apply_all is not None:
            self.apply_all = apply_all
        if products is not None:
            self.products = products

    @property
    def uom(self):
        """Gets the uom of this RefineryProductPrice.  # noqa: E501


        :return: The uom of this RefineryProductPrice.  # noqa: E501
        :rtype: ProductPriceUomType
        """
        return self._uom

    @uom.setter
    def uom(self, uom):
        """Sets the uom of this RefineryProductPrice.


        :param uom: The uom of this RefineryProductPrice.  # noqa: E501
        :type: ProductPriceUomType
        """

        self._uom = uom

    @property
    def refinery_id(self):
        """Gets the refinery_id of this RefineryProductPrice.  # noqa: E501


        :return: The refinery_id of this RefineryProductPrice.  # noqa: E501
        :rtype: int
        """
        return self._refinery_id

    @refinery_id.setter
    def refinery_id(self, refinery_id):
        """Sets the refinery_id of this RefineryProductPrice.


        :param refinery_id: The refinery_id of this RefineryProductPrice.  # noqa: E501
        :type: int
        """

        self._refinery_id = refinery_id

    @property
    def apply_all(self):
        """Gets the apply_all of this RefineryProductPrice.  # noqa: E501


        :return: The apply_all of this RefineryProductPrice.  # noqa: E501
        :rtype: bool
        """
        return self._apply_all

    @apply_all.setter
    def apply_all(self, apply_all):
        """Sets the apply_all of this RefineryProductPrice.


        :param apply_all: The apply_all of this RefineryProductPrice.  # noqa: E501
        :type: bool
        """

        self._apply_all = apply_all

    @property
    def products(self):
        """Gets the products of this RefineryProductPrice.  # noqa: E501


        :return: The products of this RefineryProductPrice.  # noqa: E501
        :rtype: list[RefineryProductPriceItem]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this RefineryProductPrice.


        :param products: The products of this RefineryProductPrice.  # noqa: E501
        :type: list[RefineryProductPriceItem]
        """

        self._products = products

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
        if issubclass(RefineryProductPrice, dict):
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
        if not isinstance(other, RefineryProductPrice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
