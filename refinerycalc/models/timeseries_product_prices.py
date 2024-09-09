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

class TimeseriesProductPrices(object):
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
        'alkylate': 'float',
        'asphalt': 'float',
        'benzene': 'float',
        'butane': 'float',
        'coke': 'float',
        'cumene': 'float',
        'gas_oil': 'float',
        'h2_fuel': 'float',
        'h2_prod': 'float',
        'heating_oil': 'float',
        'heavy_fuel_oil': 'float',
        'kerosene': 'float',
        'lubes': 'float',
        'methanol': 'float',
        'mtbe': 'float',
        'naphtha': 'float',
        'natural_gas': 'float',
        'pitch': 'float',
        'prem_gasoline': 'float',
        'propane': 'float',
        'refinery_gas': 'float',
        'reg_gasoline': 'float',
        'sour_diesel': 'float',
        'sour_gas_oil': 'float',
        'sour_resid': 'float',
        'sulfur': 'float',
        'toluene': 'float',
        'ulsd': 'float',
        'xylene': 'float',
        'lsfo': 'float',
        'msfo': 'float'
    }

    attribute_map = {
        'alkylate': 'alkylate',
        'asphalt': 'asphalt',
        'benzene': 'benzene',
        'butane': 'butane',
        'coke': 'coke',
        'cumene': 'cumene',
        'gas_oil': 'gasOil',
        'h2_fuel': 'h2Fuel',
        'h2_prod': 'h2Prod',
        'heating_oil': 'heatingOil',
        'heavy_fuel_oil': 'heavyFuelOil',
        'kerosene': 'kerosene',
        'lubes': 'lubes',
        'methanol': 'methanol',
        'mtbe': 'mtbe',
        'naphtha': 'naphtha',
        'natural_gas': 'naturalGas',
        'pitch': 'pitch',
        'prem_gasoline': 'premGasoline',
        'propane': 'propane',
        'refinery_gas': 'refineryGas',
        'reg_gasoline': 'regGasoline',
        'sour_diesel': 'sourDiesel',
        'sour_gas_oil': 'sourGasOil',
        'sour_resid': 'sourResid',
        'sulfur': 'sulfur',
        'toluene': 'toluene',
        'ulsd': 'ulsd',
        'xylene': 'xylene',
        'lsfo': 'lsfo',
        'msfo': 'msfo'
    }

    def __init__(self, alkylate=None, asphalt=None, benzene=None, butane=None, coke=None, cumene=None, gas_oil=None, h2_fuel=None, h2_prod=None, heating_oil=None, heavy_fuel_oil=None, kerosene=None, lubes=None, methanol=None, mtbe=None, naphtha=None, natural_gas=None, pitch=None, prem_gasoline=None, propane=None, refinery_gas=None, reg_gasoline=None, sour_diesel=None, sour_gas_oil=None, sour_resid=None, sulfur=None, toluene=None, ulsd=None, xylene=None, lsfo=None, msfo=None):  # noqa: E501
        """TimeseriesProductPrices - a model defined in Swagger"""  # noqa: E501
        self._alkylate = None
        self._asphalt = None
        self._benzene = None
        self._butane = None
        self._coke = None
        self._cumene = None
        self._gas_oil = None
        self._h2_fuel = None
        self._h2_prod = None
        self._heating_oil = None
        self._heavy_fuel_oil = None
        self._kerosene = None
        self._lubes = None
        self._methanol = None
        self._mtbe = None
        self._naphtha = None
        self._natural_gas = None
        self._pitch = None
        self._prem_gasoline = None
        self._propane = None
        self._refinery_gas = None
        self._reg_gasoline = None
        self._sour_diesel = None
        self._sour_gas_oil = None
        self._sour_resid = None
        self._sulfur = None
        self._toluene = None
        self._ulsd = None
        self._xylene = None
        self._lsfo = None
        self._msfo = None
        self.discriminator = None
        if alkylate is not None:
            self.alkylate = alkylate
        if asphalt is not None:
            self.asphalt = asphalt
        if benzene is not None:
            self.benzene = benzene
        if butane is not None:
            self.butane = butane
        if coke is not None:
            self.coke = coke
        if cumene is not None:
            self.cumene = cumene
        if gas_oil is not None:
            self.gas_oil = gas_oil
        if h2_fuel is not None:
            self.h2_fuel = h2_fuel
        if h2_prod is not None:
            self.h2_prod = h2_prod
        if heating_oil is not None:
            self.heating_oil = heating_oil
        if heavy_fuel_oil is not None:
            self.heavy_fuel_oil = heavy_fuel_oil
        if kerosene is not None:
            self.kerosene = kerosene
        if lubes is not None:
            self.lubes = lubes
        if methanol is not None:
            self.methanol = methanol
        if mtbe is not None:
            self.mtbe = mtbe
        if naphtha is not None:
            self.naphtha = naphtha
        if natural_gas is not None:
            self.natural_gas = natural_gas
        if pitch is not None:
            self.pitch = pitch
        if prem_gasoline is not None:
            self.prem_gasoline = prem_gasoline
        if propane is not None:
            self.propane = propane
        if refinery_gas is not None:
            self.refinery_gas = refinery_gas
        if reg_gasoline is not None:
            self.reg_gasoline = reg_gasoline
        if sour_diesel is not None:
            self.sour_diesel = sour_diesel
        if sour_gas_oil is not None:
            self.sour_gas_oil = sour_gas_oil
        if sour_resid is not None:
            self.sour_resid = sour_resid
        if sulfur is not None:
            self.sulfur = sulfur
        if toluene is not None:
            self.toluene = toluene
        if ulsd is not None:
            self.ulsd = ulsd
        if xylene is not None:
            self.xylene = xylene
        if lsfo is not None:
            self.lsfo = lsfo
        if msfo is not None:
            self.msfo = msfo

    @property
    def alkylate(self):
        """Gets the alkylate of this TimeseriesProductPrices.  # noqa: E501


        :return: The alkylate of this TimeseriesProductPrices.  # noqa: E501
        :rtype: float
        """
        return self._alkylate

    @alkylate.setter
    def alkylate(self, alkylate):
        """Sets the alkylate of this TimeseriesProductPrices.


        :param alkylate: The alkylate of this TimeseriesProductPrices.  # noqa: E501
        :type: float
        """

        self._alkylate = alkylate

    @property
    def asphalt(self):
        """Gets the asphalt of this TimeseriesProductPrices.  # noqa: E501


        :return: The asphalt of this TimeseriesProductPrices.  # noqa: E501
        :rtype: float
        """
        return self._asphalt

    @asphalt.setter
    def asphalt(self, asphalt):
        """Sets the asphalt of this TimeseriesProductPrices.


        :param asphalt: The asphalt of this TimeseriesProductPrices.  # noqa: E501
        :type: float
        """

        self._asphalt = asphalt

    @property
    def benzene(self):
        """Gets the benzene of this TimeseriesProductPrices.  # noqa: E501


        :return: The benzene of this TimeseriesProductPrices.  # noqa: E501
        :rtype: float
        """
        return self._benzene

    @benzene.setter
    def benzene(self, benzene):
        """Sets the benzene of this TimeseriesProductPrices.


        :param benzene: The benzene of this TimeseriesProductPrices.  # noqa: E501
        :type: float
        """

        self._benzene = benzene

    @property
    def butane(self):
        """Gets the butane of this TimeseriesProductPrices.  # noqa: E501


        :return: The butane of this TimeseriesProductPrices.  # noqa: E501
        :rtype: float
        """
        return self._butane

    @butane.setter
    def butane(self, butane):
        """Sets the butane of this TimeseriesProductPrices.


        :param butane: The butane of this TimeseriesProductPrices.  # noqa: E501
        :type: float
        """

        self._butane = butane

    @property
    def coke(self):
        """Gets the coke of this TimeseriesProductPrices.  # noqa: E501


        :return: The coke of this TimeseriesProductPrices.  # noqa: E501
        :rtype: float
        """
        return self._coke

    @coke.setter
    def coke(self, coke):
        """Sets the coke of this TimeseriesProductPrices.


        :param coke: The coke of this TimeseriesProductPrices.  # noqa: E501
        :type: float
        """

        self._coke = coke

    @property
    def cumene(self):
        """Gets the cumene of this TimeseriesProductPrices.  # noqa: E501


        :return: The cumene of this TimeseriesProductPrices.  # noqa: E501
        :rtype: float
        """
        return self._cumene

    @cumene.setter
    def cumene(self, cumene):
        """Sets the cumene of this TimeseriesProductPrices.


        :param cumene: The cumene of this TimeseriesProductPrices.  # noqa: E501
        :type: float
        """

        self._cumene = cumene

    @property
    def gas_oil(self):
        """Gets the gas_oil of this TimeseriesProductPrices.  # noqa: E501


        :return: The gas_oil of this TimeseriesProductPrices.  # noqa: E501
        :rtype: float
        """
        return self._gas_oil

    @gas_oil.setter
    def gas_oil(self, gas_oil):
        """Sets the gas_oil of this TimeseriesProductPrices.


        :param gas_oil: The gas_oil of this TimeseriesProductPrices.  # noqa: E501
        :type: float
        """

        self._gas_oil = gas_oil

    @property
    def h2_fuel(self):
        """Gets the h2_fuel of this TimeseriesProductPrices.  # noqa: E501


        :return: The h2_fuel of this TimeseriesProductPrices.  # noqa: E501
        :rtype: float
        """
        return self._h2_fuel

    @h2_fuel.setter
    def h2_fuel(self, h2_fuel):
        """Sets the h2_fuel of this TimeseriesProductPrices.


        :param h2_fuel: The h2_fuel of this TimeseriesProductPrices.  # noqa: E501
        :type: float
        """

        self._h2_fuel = h2_fuel

    @property
    def h2_prod(self):
        """Gets the h2_prod of this TimeseriesProductPrices.  # noqa: E501


        :return: The h2_prod of this TimeseriesProductPrices.  # noqa: E501
        :rtype: float
        """
        return self._h2_prod

    @h2_prod.setter
    def h2_prod(self, h2_prod):
        """Sets the h2_prod of this TimeseriesProductPrices.


        :param h2_prod: The h2_prod of this TimeseriesProductPrices.  # noqa: E501
        :type: float
        """

        self._h2_prod = h2_prod

    @property
    def heating_oil(self):
        """Gets the heating_oil of this TimeseriesProductPrices.  # noqa: E501


        :return: The heating_oil of this TimeseriesProductPrices.  # noqa: E501
        :rtype: float
        """
        return self._heating_oil

    @heating_oil.setter
    def heating_oil(self, heating_oil):
        """Sets the heating_oil of this TimeseriesProductPrices.


        :param heating_oil: The heating_oil of this TimeseriesProductPrices.  # noqa: E501
        :type: float
        """

        self._heating_oil = heating_oil

    @property
    def heavy_fuel_oil(self):
        """Gets the heavy_fuel_oil of this TimeseriesProductPrices.  # noqa: E501


        :return: The heavy_fuel_oil of this TimeseriesProductPrices.  # noqa: E501
        :rtype: float
        """
        return self._heavy_fuel_oil

    @heavy_fuel_oil.setter
    def heavy_fuel_oil(self, heavy_fuel_oil):
        """Sets the heavy_fuel_oil of this TimeseriesProductPrices.


        :param heavy_fuel_oil: The heavy_fuel_oil of this TimeseriesProductPrices.  # noqa: E501
        :type: float
        """

        self._heavy_fuel_oil = heavy_fuel_oil

    @property
    def kerosene(self):
        """Gets the kerosene of this TimeseriesProductPrices.  # noqa: E501


        :return: The kerosene of this TimeseriesProductPrices.  # noqa: E501
        :rtype: float
        """
        return self._kerosene

    @kerosene.setter
    def kerosene(self, kerosene):
        """Sets the kerosene of this TimeseriesProductPrices.


        :param kerosene: The kerosene of this TimeseriesProductPrices.  # noqa: E501
        :type: float
        """

        self._kerosene = kerosene

    @property
    def lubes(self):
        """Gets the lubes of this TimeseriesProductPrices.  # noqa: E501


        :return: The lubes of this TimeseriesProductPrices.  # noqa: E501
        :rtype: float
        """
        return self._lubes

    @lubes.setter
    def lubes(self, lubes):
        """Sets the lubes of this TimeseriesProductPrices.


        :param lubes: The lubes of this TimeseriesProductPrices.  # noqa: E501
        :type: float
        """

        self._lubes = lubes

    @property
    def methanol(self):
        """Gets the methanol of this TimeseriesProductPrices.  # noqa: E501


        :return: The methanol of this TimeseriesProductPrices.  # noqa: E501
        :rtype: float
        """
        return self._methanol

    @methanol.setter
    def methanol(self, methanol):
        """Sets the methanol of this TimeseriesProductPrices.


        :param methanol: The methanol of this TimeseriesProductPrices.  # noqa: E501
        :type: float
        """

        self._methanol = methanol

    @property
    def mtbe(self):
        """Gets the mtbe of this TimeseriesProductPrices.  # noqa: E501


        :return: The mtbe of this TimeseriesProductPrices.  # noqa: E501
        :rtype: float
        """
        return self._mtbe

    @mtbe.setter
    def mtbe(self, mtbe):
        """Sets the mtbe of this TimeseriesProductPrices.


        :param mtbe: The mtbe of this TimeseriesProductPrices.  # noqa: E501
        :type: float
        """

        self._mtbe = mtbe

    @property
    def naphtha(self):
        """Gets the naphtha of this TimeseriesProductPrices.  # noqa: E501


        :return: The naphtha of this TimeseriesProductPrices.  # noqa: E501
        :rtype: float
        """
        return self._naphtha

    @naphtha.setter
    def naphtha(self, naphtha):
        """Sets the naphtha of this TimeseriesProductPrices.


        :param naphtha: The naphtha of this TimeseriesProductPrices.  # noqa: E501
        :type: float
        """

        self._naphtha = naphtha

    @property
    def natural_gas(self):
        """Gets the natural_gas of this TimeseriesProductPrices.  # noqa: E501


        :return: The natural_gas of this TimeseriesProductPrices.  # noqa: E501
        :rtype: float
        """
        return self._natural_gas

    @natural_gas.setter
    def natural_gas(self, natural_gas):
        """Sets the natural_gas of this TimeseriesProductPrices.


        :param natural_gas: The natural_gas of this TimeseriesProductPrices.  # noqa: E501
        :type: float
        """

        self._natural_gas = natural_gas

    @property
    def pitch(self):
        """Gets the pitch of this TimeseriesProductPrices.  # noqa: E501


        :return: The pitch of this TimeseriesProductPrices.  # noqa: E501
        :rtype: float
        """
        return self._pitch

    @pitch.setter
    def pitch(self, pitch):
        """Sets the pitch of this TimeseriesProductPrices.


        :param pitch: The pitch of this TimeseriesProductPrices.  # noqa: E501
        :type: float
        """

        self._pitch = pitch

    @property
    def prem_gasoline(self):
        """Gets the prem_gasoline of this TimeseriesProductPrices.  # noqa: E501


        :return: The prem_gasoline of this TimeseriesProductPrices.  # noqa: E501
        :rtype: float
        """
        return self._prem_gasoline

    @prem_gasoline.setter
    def prem_gasoline(self, prem_gasoline):
        """Sets the prem_gasoline of this TimeseriesProductPrices.


        :param prem_gasoline: The prem_gasoline of this TimeseriesProductPrices.  # noqa: E501
        :type: float
        """

        self._prem_gasoline = prem_gasoline

    @property
    def propane(self):
        """Gets the propane of this TimeseriesProductPrices.  # noqa: E501


        :return: The propane of this TimeseriesProductPrices.  # noqa: E501
        :rtype: float
        """
        return self._propane

    @propane.setter
    def propane(self, propane):
        """Sets the propane of this TimeseriesProductPrices.


        :param propane: The propane of this TimeseriesProductPrices.  # noqa: E501
        :type: float
        """

        self._propane = propane

    @property
    def refinery_gas(self):
        """Gets the refinery_gas of this TimeseriesProductPrices.  # noqa: E501


        :return: The refinery_gas of this TimeseriesProductPrices.  # noqa: E501
        :rtype: float
        """
        return self._refinery_gas

    @refinery_gas.setter
    def refinery_gas(self, refinery_gas):
        """Sets the refinery_gas of this TimeseriesProductPrices.


        :param refinery_gas: The refinery_gas of this TimeseriesProductPrices.  # noqa: E501
        :type: float
        """

        self._refinery_gas = refinery_gas

    @property
    def reg_gasoline(self):
        """Gets the reg_gasoline of this TimeseriesProductPrices.  # noqa: E501


        :return: The reg_gasoline of this TimeseriesProductPrices.  # noqa: E501
        :rtype: float
        """
        return self._reg_gasoline

    @reg_gasoline.setter
    def reg_gasoline(self, reg_gasoline):
        """Sets the reg_gasoline of this TimeseriesProductPrices.


        :param reg_gasoline: The reg_gasoline of this TimeseriesProductPrices.  # noqa: E501
        :type: float
        """

        self._reg_gasoline = reg_gasoline

    @property
    def sour_diesel(self):
        """Gets the sour_diesel of this TimeseriesProductPrices.  # noqa: E501


        :return: The sour_diesel of this TimeseriesProductPrices.  # noqa: E501
        :rtype: float
        """
        return self._sour_diesel

    @sour_diesel.setter
    def sour_diesel(self, sour_diesel):
        """Sets the sour_diesel of this TimeseriesProductPrices.


        :param sour_diesel: The sour_diesel of this TimeseriesProductPrices.  # noqa: E501
        :type: float
        """

        self._sour_diesel = sour_diesel

    @property
    def sour_gas_oil(self):
        """Gets the sour_gas_oil of this TimeseriesProductPrices.  # noqa: E501


        :return: The sour_gas_oil of this TimeseriesProductPrices.  # noqa: E501
        :rtype: float
        """
        return self._sour_gas_oil

    @sour_gas_oil.setter
    def sour_gas_oil(self, sour_gas_oil):
        """Sets the sour_gas_oil of this TimeseriesProductPrices.


        :param sour_gas_oil: The sour_gas_oil of this TimeseriesProductPrices.  # noqa: E501
        :type: float
        """

        self._sour_gas_oil = sour_gas_oil

    @property
    def sour_resid(self):
        """Gets the sour_resid of this TimeseriesProductPrices.  # noqa: E501


        :return: The sour_resid of this TimeseriesProductPrices.  # noqa: E501
        :rtype: float
        """
        return self._sour_resid

    @sour_resid.setter
    def sour_resid(self, sour_resid):
        """Sets the sour_resid of this TimeseriesProductPrices.


        :param sour_resid: The sour_resid of this TimeseriesProductPrices.  # noqa: E501
        :type: float
        """

        self._sour_resid = sour_resid

    @property
    def sulfur(self):
        """Gets the sulfur of this TimeseriesProductPrices.  # noqa: E501


        :return: The sulfur of this TimeseriesProductPrices.  # noqa: E501
        :rtype: float
        """
        return self._sulfur

    @sulfur.setter
    def sulfur(self, sulfur):
        """Sets the sulfur of this TimeseriesProductPrices.


        :param sulfur: The sulfur of this TimeseriesProductPrices.  # noqa: E501
        :type: float
        """

        self._sulfur = sulfur

    @property
    def toluene(self):
        """Gets the toluene of this TimeseriesProductPrices.  # noqa: E501


        :return: The toluene of this TimeseriesProductPrices.  # noqa: E501
        :rtype: float
        """
        return self._toluene

    @toluene.setter
    def toluene(self, toluene):
        """Sets the toluene of this TimeseriesProductPrices.


        :param toluene: The toluene of this TimeseriesProductPrices.  # noqa: E501
        :type: float
        """

        self._toluene = toluene

    @property
    def ulsd(self):
        """Gets the ulsd of this TimeseriesProductPrices.  # noqa: E501


        :return: The ulsd of this TimeseriesProductPrices.  # noqa: E501
        :rtype: float
        """
        return self._ulsd

    @ulsd.setter
    def ulsd(self, ulsd):
        """Sets the ulsd of this TimeseriesProductPrices.


        :param ulsd: The ulsd of this TimeseriesProductPrices.  # noqa: E501
        :type: float
        """

        self._ulsd = ulsd

    @property
    def xylene(self):
        """Gets the xylene of this TimeseriesProductPrices.  # noqa: E501


        :return: The xylene of this TimeseriesProductPrices.  # noqa: E501
        :rtype: float
        """
        return self._xylene

    @xylene.setter
    def xylene(self, xylene):
        """Sets the xylene of this TimeseriesProductPrices.


        :param xylene: The xylene of this TimeseriesProductPrices.  # noqa: E501
        :type: float
        """

        self._xylene = xylene

    @property
    def lsfo(self):
        """Gets the lsfo of this TimeseriesProductPrices.  # noqa: E501


        :return: The lsfo of this TimeseriesProductPrices.  # noqa: E501
        :rtype: float
        """
        return self._lsfo

    @lsfo.setter
    def lsfo(self, lsfo):
        """Sets the lsfo of this TimeseriesProductPrices.


        :param lsfo: The lsfo of this TimeseriesProductPrices.  # noqa: E501
        :type: float
        """

        self._lsfo = lsfo

    @property
    def msfo(self):
        """Gets the msfo of this TimeseriesProductPrices.  # noqa: E501


        :return: The msfo of this TimeseriesProductPrices.  # noqa: E501
        :rtype: float
        """
        return self._msfo

    @msfo.setter
    def msfo(self, msfo):
        """Sets the msfo of this TimeseriesProductPrices.


        :param msfo: The msfo of this TimeseriesProductPrices.  # noqa: E501
        :type: float
        """

        self._msfo = msfo

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
        if issubclass(TimeseriesProductPrices, dict):
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
        if not isinstance(other, TimeseriesProductPrices):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other