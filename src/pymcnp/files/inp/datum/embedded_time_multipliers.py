from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors


class EmbeddedTimeMultipliers(Datum):
    """
    ``EmbeddedTimeMultipliers`` represents INP embedded elemental
    edits time multipliers.

    ``EmbeddedTimeMultipliers`` inherits attributes from ``Datum``. It
    represents the INP embedded embedded elemental edits time multipliers data
    card syntax element.

    Attributes:
        multipliers: Tuple of time multipliers.
    """

    def __init__(self, multipliers: tuple[float], suffix: types.McnpInteger):
        """
        ``__init__`` initializes ``EmbeddedTimeMultipliers``.

        Parameters:
            multipliers: Tuple of time multipliers.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
            MCNPSemanticError: INVALID_DATUM_SUFFIX
        """

        for parameter in multipliers:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)

        _card.Card.__init__(self, f'embtm{suffix}')
        self.mnemonic = DatumMnemonic.EMBEDDED_TIME_MULTIPLIERS
        self.parameters = multipliers
        self.suffix = suffix

        self.multipliers = multipliers
