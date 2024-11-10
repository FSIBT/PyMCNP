from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import errors


class ThermalTimes(Datum):
    """
    ``ThermalTimes`` represents INP thermal times data cards.

    ``ThermalTimes`` inherits attributes from ``Datum``. It represents the INP
    thermal times data card syntax element.

    Attributes:
        times: Times in shakes.
    """

    def __init__(self, times: tuple[int]):
        """
        ``__init__`` initializes ``FreeGasThermalTemperature``.

        Parameters:
            times: Times in shakes.
        """

        if times is None or not times:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        for time in times:
            if time is None or not (0 <= time <= 99):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, 'thtme')
        self.mnemonic = DatumMnemonic.THERMAL_TIMES
        self.parameters = times

        self.times = times
