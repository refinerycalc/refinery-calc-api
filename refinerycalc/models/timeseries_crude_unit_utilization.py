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

class TimeseriesCrudeUnitUtilization(object):
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
        'alky': 'str',
        'aromatics': 'str',
        'asphalt': 'str',
        'coker': 'str',
        'crude': 'str',
        'dist_ht': 'str',
        'fcc': 'str',
        'gas_ht': 'str',
        'goht': 'str',
        'h2': 'str',
        'hydrk': 'str',
        'hydrk_rsd': 'str',
        'isom': 'str',
        'kero_ht': 'str',
        'lubes': 'str',
        'naph_ht': 'str',
        'reformer': 'str',
        'sda': 'str',
        'sulftons': 'str',
        'vacuum': 'str',
        'visbreaker': 'str'
    }

    attribute_map = {
        'alky': 'alky',
        'aromatics': 'aromatics',
        'asphalt': 'asphalt',
        'coker': 'coker',
        'crude': 'crude',
        'dist_ht': 'distHT',
        'fcc': 'fcc',
        'gas_ht': 'gasHT',
        'goht': 'goht',
        'h2': 'h2',
        'hydrk': 'hydrk',
        'hydrk_rsd': 'hydrkRsd',
        'isom': 'isom',
        'kero_ht': 'keroHT',
        'lubes': 'lubes',
        'naph_ht': 'naphHT',
        'reformer': 'reformer',
        'sda': 'sda',
        'sulftons': 'sulftons',
        'vacuum': 'vacuum',
        'visbreaker': 'visbreaker'
    }

    def __init__(self, alky=None, aromatics=None, asphalt=None, coker=None, crude=None, dist_ht=None, fcc=None, gas_ht=None, goht=None, h2=None, hydrk=None, hydrk_rsd=None, isom=None, kero_ht=None, lubes=None, naph_ht=None, reformer=None, sda=None, sulftons=None, vacuum=None, visbreaker=None):  # noqa: E501
        """TimeseriesCrudeUnitUtilization - a model defined in Swagger"""  # noqa: E501
        self._alky = None
        self._aromatics = None
        self._asphalt = None
        self._coker = None
        self._crude = None
        self._dist_ht = None
        self._fcc = None
        self._gas_ht = None
        self._goht = None
        self._h2 = None
        self._hydrk = None
        self._hydrk_rsd = None
        self._isom = None
        self._kero_ht = None
        self._lubes = None
        self._naph_ht = None
        self._reformer = None
        self._sda = None
        self._sulftons = None
        self._vacuum = None
        self._visbreaker = None
        self.discriminator = None
        if alky is not None:
            self.alky = alky
        if aromatics is not None:
            self.aromatics = aromatics
        if asphalt is not None:
            self.asphalt = asphalt
        if coker is not None:
            self.coker = coker
        if crude is not None:
            self.crude = crude
        if dist_ht is not None:
            self.dist_ht = dist_ht
        if fcc is not None:
            self.fcc = fcc
        if gas_ht is not None:
            self.gas_ht = gas_ht
        if goht is not None:
            self.goht = goht
        if h2 is not None:
            self.h2 = h2
        if hydrk is not None:
            self.hydrk = hydrk
        if hydrk_rsd is not None:
            self.hydrk_rsd = hydrk_rsd
        if isom is not None:
            self.isom = isom
        if kero_ht is not None:
            self.kero_ht = kero_ht
        if lubes is not None:
            self.lubes = lubes
        if naph_ht is not None:
            self.naph_ht = naph_ht
        if reformer is not None:
            self.reformer = reformer
        if sda is not None:
            self.sda = sda
        if sulftons is not None:
            self.sulftons = sulftons
        if vacuum is not None:
            self.vacuum = vacuum
        if visbreaker is not None:
            self.visbreaker = visbreaker

    @property
    def alky(self):
        """Gets the alky of this TimeseriesCrudeUnitUtilization.  # noqa: E501


        :return: The alky of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :rtype: str
        """
        return self._alky

    @alky.setter
    def alky(self, alky):
        """Sets the alky of this TimeseriesCrudeUnitUtilization.


        :param alky: The alky of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :type: str
        """

        self._alky = alky

    @property
    def aromatics(self):
        """Gets the aromatics of this TimeseriesCrudeUnitUtilization.  # noqa: E501


        :return: The aromatics of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :rtype: str
        """
        return self._aromatics

    @aromatics.setter
    def aromatics(self, aromatics):
        """Sets the aromatics of this TimeseriesCrudeUnitUtilization.


        :param aromatics: The aromatics of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :type: str
        """

        self._aromatics = aromatics

    @property
    def asphalt(self):
        """Gets the asphalt of this TimeseriesCrudeUnitUtilization.  # noqa: E501


        :return: The asphalt of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :rtype: str
        """
        return self._asphalt

    @asphalt.setter
    def asphalt(self, asphalt):
        """Sets the asphalt of this TimeseriesCrudeUnitUtilization.


        :param asphalt: The asphalt of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :type: str
        """

        self._asphalt = asphalt

    @property
    def coker(self):
        """Gets the coker of this TimeseriesCrudeUnitUtilization.  # noqa: E501


        :return: The coker of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :rtype: str
        """
        return self._coker

    @coker.setter
    def coker(self, coker):
        """Sets the coker of this TimeseriesCrudeUnitUtilization.


        :param coker: The coker of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :type: str
        """

        self._coker = coker

    @property
    def crude(self):
        """Gets the crude of this TimeseriesCrudeUnitUtilization.  # noqa: E501


        :return: The crude of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :rtype: str
        """
        return self._crude

    @crude.setter
    def crude(self, crude):
        """Sets the crude of this TimeseriesCrudeUnitUtilization.


        :param crude: The crude of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :type: str
        """

        self._crude = crude

    @property
    def dist_ht(self):
        """Gets the dist_ht of this TimeseriesCrudeUnitUtilization.  # noqa: E501


        :return: The dist_ht of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :rtype: str
        """
        return self._dist_ht

    @dist_ht.setter
    def dist_ht(self, dist_ht):
        """Sets the dist_ht of this TimeseriesCrudeUnitUtilization.


        :param dist_ht: The dist_ht of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :type: str
        """

        self._dist_ht = dist_ht

    @property
    def fcc(self):
        """Gets the fcc of this TimeseriesCrudeUnitUtilization.  # noqa: E501


        :return: The fcc of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :rtype: str
        """
        return self._fcc

    @fcc.setter
    def fcc(self, fcc):
        """Sets the fcc of this TimeseriesCrudeUnitUtilization.


        :param fcc: The fcc of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :type: str
        """

        self._fcc = fcc

    @property
    def gas_ht(self):
        """Gets the gas_ht of this TimeseriesCrudeUnitUtilization.  # noqa: E501


        :return: The gas_ht of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :rtype: str
        """
        return self._gas_ht

    @gas_ht.setter
    def gas_ht(self, gas_ht):
        """Sets the gas_ht of this TimeseriesCrudeUnitUtilization.


        :param gas_ht: The gas_ht of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :type: str
        """

        self._gas_ht = gas_ht

    @property
    def goht(self):
        """Gets the goht of this TimeseriesCrudeUnitUtilization.  # noqa: E501


        :return: The goht of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :rtype: str
        """
        return self._goht

    @goht.setter
    def goht(self, goht):
        """Sets the goht of this TimeseriesCrudeUnitUtilization.


        :param goht: The goht of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :type: str
        """

        self._goht = goht

    @property
    def h2(self):
        """Gets the h2 of this TimeseriesCrudeUnitUtilization.  # noqa: E501


        :return: The h2 of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :rtype: str
        """
        return self._h2

    @h2.setter
    def h2(self, h2):
        """Sets the h2 of this TimeseriesCrudeUnitUtilization.


        :param h2: The h2 of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :type: str
        """

        self._h2 = h2

    @property
    def hydrk(self):
        """Gets the hydrk of this TimeseriesCrudeUnitUtilization.  # noqa: E501


        :return: The hydrk of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :rtype: str
        """
        return self._hydrk

    @hydrk.setter
    def hydrk(self, hydrk):
        """Sets the hydrk of this TimeseriesCrudeUnitUtilization.


        :param hydrk: The hydrk of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :type: str
        """

        self._hydrk = hydrk

    @property
    def hydrk_rsd(self):
        """Gets the hydrk_rsd of this TimeseriesCrudeUnitUtilization.  # noqa: E501


        :return: The hydrk_rsd of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :rtype: str
        """
        return self._hydrk_rsd

    @hydrk_rsd.setter
    def hydrk_rsd(self, hydrk_rsd):
        """Sets the hydrk_rsd of this TimeseriesCrudeUnitUtilization.


        :param hydrk_rsd: The hydrk_rsd of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :type: str
        """

        self._hydrk_rsd = hydrk_rsd

    @property
    def isom(self):
        """Gets the isom of this TimeseriesCrudeUnitUtilization.  # noqa: E501


        :return: The isom of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :rtype: str
        """
        return self._isom

    @isom.setter
    def isom(self, isom):
        """Sets the isom of this TimeseriesCrudeUnitUtilization.


        :param isom: The isom of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :type: str
        """

        self._isom = isom

    @property
    def kero_ht(self):
        """Gets the kero_ht of this TimeseriesCrudeUnitUtilization.  # noqa: E501


        :return: The kero_ht of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :rtype: str
        """
        return self._kero_ht

    @kero_ht.setter
    def kero_ht(self, kero_ht):
        """Sets the kero_ht of this TimeseriesCrudeUnitUtilization.


        :param kero_ht: The kero_ht of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :type: str
        """

        self._kero_ht = kero_ht

    @property
    def lubes(self):
        """Gets the lubes of this TimeseriesCrudeUnitUtilization.  # noqa: E501


        :return: The lubes of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :rtype: str
        """
        return self._lubes

    @lubes.setter
    def lubes(self, lubes):
        """Sets the lubes of this TimeseriesCrudeUnitUtilization.


        :param lubes: The lubes of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :type: str
        """

        self._lubes = lubes

    @property
    def naph_ht(self):
        """Gets the naph_ht of this TimeseriesCrudeUnitUtilization.  # noqa: E501


        :return: The naph_ht of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :rtype: str
        """
        return self._naph_ht

    @naph_ht.setter
    def naph_ht(self, naph_ht):
        """Sets the naph_ht of this TimeseriesCrudeUnitUtilization.


        :param naph_ht: The naph_ht of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :type: str
        """

        self._naph_ht = naph_ht

    @property
    def reformer(self):
        """Gets the reformer of this TimeseriesCrudeUnitUtilization.  # noqa: E501


        :return: The reformer of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :rtype: str
        """
        return self._reformer

    @reformer.setter
    def reformer(self, reformer):
        """Sets the reformer of this TimeseriesCrudeUnitUtilization.


        :param reformer: The reformer of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :type: str
        """

        self._reformer = reformer

    @property
    def sda(self):
        """Gets the sda of this TimeseriesCrudeUnitUtilization.  # noqa: E501


        :return: The sda of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :rtype: str
        """
        return self._sda

    @sda.setter
    def sda(self, sda):
        """Sets the sda of this TimeseriesCrudeUnitUtilization.


        :param sda: The sda of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :type: str
        """

        self._sda = sda

    @property
    def sulftons(self):
        """Gets the sulftons of this TimeseriesCrudeUnitUtilization.  # noqa: E501


        :return: The sulftons of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :rtype: str
        """
        return self._sulftons

    @sulftons.setter
    def sulftons(self, sulftons):
        """Sets the sulftons of this TimeseriesCrudeUnitUtilization.


        :param sulftons: The sulftons of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :type: str
        """

        self._sulftons = sulftons

    @property
    def vacuum(self):
        """Gets the vacuum of this TimeseriesCrudeUnitUtilization.  # noqa: E501


        :return: The vacuum of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :rtype: str
        """
        return self._vacuum

    @vacuum.setter
    def vacuum(self, vacuum):
        """Sets the vacuum of this TimeseriesCrudeUnitUtilization.


        :param vacuum: The vacuum of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :type: str
        """

        self._vacuum = vacuum

    @property
    def visbreaker(self):
        """Gets the visbreaker of this TimeseriesCrudeUnitUtilization.  # noqa: E501


        :return: The visbreaker of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :rtype: str
        """
        return self._visbreaker

    @visbreaker.setter
    def visbreaker(self, visbreaker):
        """Sets the visbreaker of this TimeseriesCrudeUnitUtilization.


        :param visbreaker: The visbreaker of this TimeseriesCrudeUnitUtilization.  # noqa: E501
        :type: str
        """

        self._visbreaker = visbreaker

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
        if issubclass(TimeseriesCrudeUnitUtilization, dict):
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
        if not isinstance(other, TimeseriesCrudeUnitUtilization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other