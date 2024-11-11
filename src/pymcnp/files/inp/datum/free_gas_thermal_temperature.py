from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors


class FreeGasThermalTemperature(Datum):
    """
    ``FreeGasThermalTemperature`` represents INP free-gas thermal temperature
    data cards.

    ``FreeGasThermalTemperature`` inherits attributes from ``Datum``. It
    represents the INP free-gas thermal temperature data card syntax element.

    Attributes:
        suffix: Index of time on the thermal time.
        temperatures: Temperatures of cells at given time indexes.
    """

    def __init__(self, suffix: types.McnpInteger, temperatures: types.McnpReal):
        """
        ``__init__`` initializes ``FreeGasThermalTemperature``.

        Parameters:
            suffix: Index of time on the thermal time.
            temperatures: Temperatures of cells at given time indexes.
        """

        if suffix is None or not (0 <= suffix <= 99):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)

        if temperatures is None or not temperatures:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        for temperature in temperatures:
            if temperature is None or not (temperature > 0):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, f'tmp{suffix}')
        self.mnemonic = DatumMnemonic.FREE_GAS_THERMAL_TEMPERATURE
        self.parameters = temperatures
        self.suffix = suffix

        self.temperatures = temperatures
