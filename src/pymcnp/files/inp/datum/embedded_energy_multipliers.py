from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors


class EmbeddedEnergyMultipliers(Datum):
    """
    ``EmbeddedEnergyMultipliers`` represents INP embedded elemental
    edits energy multipliers.

    ``EmbeddedEnergyMultipliers`` inherits attributes from ``Datum``. It
    represents the INP embedded elemental edits energy multipliers data card
    syntax element.

    Attributes:
        multipliers: Tuple of energy multipliers.
    """

    def __init__(self, multipliers: tuple[float], suffix: types.McnpInteger):
        """
        ``__init__`` initializes ``EmbeddedEnergyMultipliers``.

        Parameters:
            multipliers: Tuple of energy multipliers.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
            MCNPSemanticError: INVALID_DATUM_SUFFIX.
        """

        for parameter in multipliers:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)

        _card.Card.__init__(self, f'embem{suffix}')
        self.mnemonic = DatumMnemonic.EMBEDDED_ENERGY_MULTIPLIERS
        self.parameters = multipliers
        self.suffix = suffix

        self.multipliers = multipliers
