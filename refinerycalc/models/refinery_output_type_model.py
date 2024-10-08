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

class RefineryOutputTypeModel(object):
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
        'refinery_id': 'int',
        'refinery_name': 'str',
        'percent_solved': 'float',
        'start_time': 'datetime',
        'stop_time': 'datetime',
        'duration_in_seconds': 'int',
        'output': 'OutputTypes'
    }

    attribute_map = {
        'refinery_id': 'refineryId',
        'refinery_name': 'refineryName',
        'percent_solved': 'percentSolved',
        'start_time': 'startTime',
        'stop_time': 'stopTime',
        'duration_in_seconds': 'durationInSeconds',
        'output': 'output'
    }

    def __init__(self, refinery_id=None, refinery_name=None, percent_solved=None, start_time=None, stop_time=None, duration_in_seconds=None, output=None):  # noqa: E501
        """RefineryOutputTypeModel - a model defined in Swagger"""  # noqa: E501
        self._refinery_id = None
        self._refinery_name = None
        self._percent_solved = None
        self._start_time = None
        self._stop_time = None
        self._duration_in_seconds = None
        self._output = None
        self.discriminator = None
        if refinery_id is not None:
            self.refinery_id = refinery_id
        if refinery_name is not None:
            self.refinery_name = refinery_name
        if percent_solved is not None:
            self.percent_solved = percent_solved
        if start_time is not None:
            self.start_time = start_time
        if stop_time is not None:
            self.stop_time = stop_time
        if duration_in_seconds is not None:
            self.duration_in_seconds = duration_in_seconds
        if output is not None:
            self.output = output

    @property
    def refinery_id(self):
        """Gets the refinery_id of this RefineryOutputTypeModel.  # noqa: E501


        :return: The refinery_id of this RefineryOutputTypeModel.  # noqa: E501
        :rtype: int
        """
        return self._refinery_id

    @refinery_id.setter
    def refinery_id(self, refinery_id):
        """Sets the refinery_id of this RefineryOutputTypeModel.


        :param refinery_id: The refinery_id of this RefineryOutputTypeModel.  # noqa: E501
        :type: int
        """

        self._refinery_id = refinery_id

    @property
    def refinery_name(self):
        """Gets the refinery_name of this RefineryOutputTypeModel.  # noqa: E501


        :return: The refinery_name of this RefineryOutputTypeModel.  # noqa: E501
        :rtype: str
        """
        return self._refinery_name

    @refinery_name.setter
    def refinery_name(self, refinery_name):
        """Sets the refinery_name of this RefineryOutputTypeModel.


        :param refinery_name: The refinery_name of this RefineryOutputTypeModel.  # noqa: E501
        :type: str
        """

        self._refinery_name = refinery_name

    @property
    def percent_solved(self):
        """Gets the percent_solved of this RefineryOutputTypeModel.  # noqa: E501


        :return: The percent_solved of this RefineryOutputTypeModel.  # noqa: E501
        :rtype: float
        """
        return self._percent_solved

    @percent_solved.setter
    def percent_solved(self, percent_solved):
        """Sets the percent_solved of this RefineryOutputTypeModel.


        :param percent_solved: The percent_solved of this RefineryOutputTypeModel.  # noqa: E501
        :type: float
        """

        self._percent_solved = percent_solved

    @property
    def start_time(self):
        """Gets the start_time of this RefineryOutputTypeModel.  # noqa: E501


        :return: The start_time of this RefineryOutputTypeModel.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this RefineryOutputTypeModel.


        :param start_time: The start_time of this RefineryOutputTypeModel.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def stop_time(self):
        """Gets the stop_time of this RefineryOutputTypeModel.  # noqa: E501


        :return: The stop_time of this RefineryOutputTypeModel.  # noqa: E501
        :rtype: datetime
        """
        return self._stop_time

    @stop_time.setter
    def stop_time(self, stop_time):
        """Sets the stop_time of this RefineryOutputTypeModel.


        :param stop_time: The stop_time of this RefineryOutputTypeModel.  # noqa: E501
        :type: datetime
        """

        self._stop_time = stop_time

    @property
    def duration_in_seconds(self):
        """Gets the duration_in_seconds of this RefineryOutputTypeModel.  # noqa: E501


        :return: The duration_in_seconds of this RefineryOutputTypeModel.  # noqa: E501
        :rtype: int
        """
        return self._duration_in_seconds

    @duration_in_seconds.setter
    def duration_in_seconds(self, duration_in_seconds):
        """Sets the duration_in_seconds of this RefineryOutputTypeModel.


        :param duration_in_seconds: The duration_in_seconds of this RefineryOutputTypeModel.  # noqa: E501
        :type: int
        """

        self._duration_in_seconds = duration_in_seconds

    @property
    def output(self):
        """Gets the output of this RefineryOutputTypeModel.  # noqa: E501


        :return: The output of this RefineryOutputTypeModel.  # noqa: E501
        :rtype: OutputTypes
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this RefineryOutputTypeModel.


        :param output: The output of this RefineryOutputTypeModel.  # noqa: E501
        :type: OutputTypes
        """

        self._output = output

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
        if issubclass(RefineryOutputTypeModel, dict):
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
        if not isinstance(other, RefineryOutputTypeModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
