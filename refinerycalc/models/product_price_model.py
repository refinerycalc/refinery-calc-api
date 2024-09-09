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

class ProductPriceModel(object):
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
        'id': 'int',
        'name': 'str',
        'value': 'float',
        'uom': 'str',
        'price_date': 'datetime',
        'region_name': 'str',
        'region_id': 'int',
        'product_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'value': 'value',
        'uom': 'uom',
        'price_date': 'priceDate',
        'region_name': 'regionName',
        'region_id': 'regionId',
        'product_id': 'productId'
    }

    def __init__(self, id=None, name=None, value=None, uom=None, price_date=None, region_name=None, region_id=None, product_id=None):  # noqa: E501
        """ProductPriceModel - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._value = None
        self._uom = None
        self._price_date = None
        self._region_name = None
        self._region_id = None
        self._product_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if uom is not None:
            self.uom = uom
        if price_date is not None:
            self.price_date = price_date
        if region_name is not None:
            self.region_name = region_name
        if region_id is not None:
            self.region_id = region_id
        if product_id is not None:
            self.product_id = product_id

    @property
    def id(self):
        """Gets the id of this ProductPriceModel.  # noqa: E501


        :return: The id of this ProductPriceModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProductPriceModel.


        :param id: The id of this ProductPriceModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ProductPriceModel.  # noqa: E501


        :return: The name of this ProductPriceModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProductPriceModel.


        :param name: The name of this ProductPriceModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """Gets the value of this ProductPriceModel.  # noqa: E501


        :return: The value of this ProductPriceModel.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ProductPriceModel.


        :param value: The value of this ProductPriceModel.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def uom(self):
        """Gets the uom of this ProductPriceModel.  # noqa: E501


        :return: The uom of this ProductPriceModel.  # noqa: E501
        :rtype: str
        """
        return self._uom

    @uom.setter
    def uom(self, uom):
        """Sets the uom of this ProductPriceModel.


        :param uom: The uom of this ProductPriceModel.  # noqa: E501
        :type: str
        """

        self._uom = uom

    @property
    def price_date(self):
        """Gets the price_date of this ProductPriceModel.  # noqa: E501


        :return: The price_date of this ProductPriceModel.  # noqa: E501
        :rtype: datetime
        """
        return self._price_date

    @price_date.setter
    def price_date(self, price_date):
        """Sets the price_date of this ProductPriceModel.


        :param price_date: The price_date of this ProductPriceModel.  # noqa: E501
        :type: datetime
        """

        self._price_date = price_date

    @property
    def region_name(self):
        """Gets the region_name of this ProductPriceModel.  # noqa: E501


        :return: The region_name of this ProductPriceModel.  # noqa: E501
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this ProductPriceModel.


        :param region_name: The region_name of this ProductPriceModel.  # noqa: E501
        :type: str
        """

        self._region_name = region_name

    @property
    def region_id(self):
        """Gets the region_id of this ProductPriceModel.  # noqa: E501


        :return: The region_id of this ProductPriceModel.  # noqa: E501
        :rtype: int
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ProductPriceModel.


        :param region_id: The region_id of this ProductPriceModel.  # noqa: E501
        :type: int
        """

        self._region_id = region_id

    @property
    def product_id(self):
        """Gets the product_id of this ProductPriceModel.  # noqa: E501


        :return: The product_id of this ProductPriceModel.  # noqa: E501
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ProductPriceModel.


        :param product_id: The product_id of this ProductPriceModel.  # noqa: E501
        :type: int
        """

        self._product_id = product_id

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
        if issubclass(ProductPriceModel, dict):
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
        if not isinstance(other, ProductPriceModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
