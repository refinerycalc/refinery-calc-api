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

class CalculatorRefineryOutputModel(object):
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
        'refinery_name': 'str',
        'output_type': 'OutputType',
        'name': 'str',
        'value': 'str',
        'description': 'str',
        'unit_of_measure': 'str',
        'display_order': 'int',
        'day_number': 'int',
        'calculator_refinery_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'refinery_name': 'refineryName',
        'output_type': 'outputType',
        'name': 'name',
        'value': 'value',
        'description': 'description',
        'unit_of_measure': 'unitOfMeasure',
        'display_order': 'displayOrder',
        'day_number': 'dayNumber',
        'calculator_refinery_id': 'calculatorRefineryId'
    }

    def __init__(self, id=None, refinery_name=None, output_type=None, name=None, value=None, description=None, unit_of_measure=None, display_order=None, day_number=None, calculator_refinery_id=None):  # noqa: E501
        """CalculatorRefineryOutputModel - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._refinery_name = None
        self._output_type = None
        self._name = None
        self._value = None
        self._description = None
        self._unit_of_measure = None
        self._display_order = None
        self._day_number = None
        self._calculator_refinery_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if refinery_name is not None:
            self.refinery_name = refinery_name
        if output_type is not None:
            self.output_type = output_type
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if description is not None:
            self.description = description
        if unit_of_measure is not None:
            self.unit_of_measure = unit_of_measure
        if display_order is not None:
            self.display_order = display_order
        if day_number is not None:
            self.day_number = day_number
        if calculator_refinery_id is not None:
            self.calculator_refinery_id = calculator_refinery_id

    @property
    def id(self):
        """Gets the id of this CalculatorRefineryOutputModel.  # noqa: E501


        :return: The id of this CalculatorRefineryOutputModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CalculatorRefineryOutputModel.


        :param id: The id of this CalculatorRefineryOutputModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def refinery_name(self):
        """Gets the refinery_name of this CalculatorRefineryOutputModel.  # noqa: E501


        :return: The refinery_name of this CalculatorRefineryOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._refinery_name

    @refinery_name.setter
    def refinery_name(self, refinery_name):
        """Sets the refinery_name of this CalculatorRefineryOutputModel.


        :param refinery_name: The refinery_name of this CalculatorRefineryOutputModel.  # noqa: E501
        :type: str
        """

        self._refinery_name = refinery_name

    @property
    def output_type(self):
        """Gets the output_type of this CalculatorRefineryOutputModel.  # noqa: E501


        :return: The output_type of this CalculatorRefineryOutputModel.  # noqa: E501
        :rtype: OutputType
        """
        return self._output_type

    @output_type.setter
    def output_type(self, output_type):
        """Sets the output_type of this CalculatorRefineryOutputModel.


        :param output_type: The output_type of this CalculatorRefineryOutputModel.  # noqa: E501
        :type: OutputType
        """

        self._output_type = output_type

    @property
    def name(self):
        """Gets the name of this CalculatorRefineryOutputModel.  # noqa: E501


        :return: The name of this CalculatorRefineryOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CalculatorRefineryOutputModel.


        :param name: The name of this CalculatorRefineryOutputModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """Gets the value of this CalculatorRefineryOutputModel.  # noqa: E501


        :return: The value of this CalculatorRefineryOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CalculatorRefineryOutputModel.


        :param value: The value of this CalculatorRefineryOutputModel.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def description(self):
        """Gets the description of this CalculatorRefineryOutputModel.  # noqa: E501


        :return: The description of this CalculatorRefineryOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CalculatorRefineryOutputModel.


        :param description: The description of this CalculatorRefineryOutputModel.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def unit_of_measure(self):
        """Gets the unit_of_measure of this CalculatorRefineryOutputModel.  # noqa: E501


        :return: The unit_of_measure of this CalculatorRefineryOutputModel.  # noqa: E501
        :rtype: str
        """
        return self._unit_of_measure

    @unit_of_measure.setter
    def unit_of_measure(self, unit_of_measure):
        """Sets the unit_of_measure of this CalculatorRefineryOutputModel.


        :param unit_of_measure: The unit_of_measure of this CalculatorRefineryOutputModel.  # noqa: E501
        :type: str
        """

        self._unit_of_measure = unit_of_measure

    @property
    def display_order(self):
        """Gets the display_order of this CalculatorRefineryOutputModel.  # noqa: E501


        :return: The display_order of this CalculatorRefineryOutputModel.  # noqa: E501
        :rtype: int
        """
        return self._display_order

    @display_order.setter
    def display_order(self, display_order):
        """Sets the display_order of this CalculatorRefineryOutputModel.


        :param display_order: The display_order of this CalculatorRefineryOutputModel.  # noqa: E501
        :type: int
        """

        self._display_order = display_order

    @property
    def day_number(self):
        """Gets the day_number of this CalculatorRefineryOutputModel.  # noqa: E501


        :return: The day_number of this CalculatorRefineryOutputModel.  # noqa: E501
        :rtype: int
        """
        return self._day_number

    @day_number.setter
    def day_number(self, day_number):
        """Sets the day_number of this CalculatorRefineryOutputModel.


        :param day_number: The day_number of this CalculatorRefineryOutputModel.  # noqa: E501
        :type: int
        """

        self._day_number = day_number

    @property
    def calculator_refinery_id(self):
        """Gets the calculator_refinery_id of this CalculatorRefineryOutputModel.  # noqa: E501


        :return: The calculator_refinery_id of this CalculatorRefineryOutputModel.  # noqa: E501
        :rtype: int
        """
        return self._calculator_refinery_id

    @calculator_refinery_id.setter
    def calculator_refinery_id(self, calculator_refinery_id):
        """Sets the calculator_refinery_id of this CalculatorRefineryOutputModel.


        :param calculator_refinery_id: The calculator_refinery_id of this CalculatorRefineryOutputModel.  # noqa: E501
        :type: int
        """

        self._calculator_refinery_id = calculator_refinery_id

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
        if issubclass(CalculatorRefineryOutputModel, dict):
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
        if not isinstance(other, CalculatorRefineryOutputModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
