from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors


class EmbeddedDoseMultipliers(Datum):
    """
    ``EmbeddedDoseMultipliers`` represents INP embedded elemental
    edits dose multipliers.

    ``EmbeddedDoseMultipliers`` iinherits attributes from ``Datum``. It
    represents the INP embedded embedded elemental edits dose multipliers data
    card syntax element.

    Attributes:
        doses: Tuple of dose multipliers.
    """

    def __init__(self, multipliers: tuple[float], suffix: types.McnpInteger):
        """
        ``__init__`` initializes ``EmbeddedDoseMultipliers``.

        Parameters:
            multipliers: Tuple of dose multipliers.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
            MCNPSemanticError: INVALID_DATUM_SUFFIX.
        """

        for parameter in multipliers:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, f'embdf{suffix}')
        self.mnemonic = DatumMnemonic.EMBEDDED_DOSE_MULTIPLIERS
        self.parameters = multipliers
        self.suffix = suffix

        self.multipliers = multipliers
