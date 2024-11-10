from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors


class EmbeddedDoseBoundaries(Datum):
    """
    ``EmbeddedDoseBoundaries`` represents INP embedded elemental edits
    dose boundaries.

    ``EmbeddedDoseBoundaries`` inherits attributes from ``Datum``. It
    represents the INP embedded embedded elemental edits dose boundaries data
    card syntax element.

    Attributes:
        doses: Tuple of dose lower bounds.
    """

    def __init__(self, doses: tuple[float], suffix: types.McnpInteger):
        """
        ``__init__`` initializes ``EmbeddedDoseBoundaries``.

        Parameters:
            doses: Tuple of dose lower bounds.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
            MCNPSemanticError: INVALID_DATUM_SUFFIX.
        """

        for parameter in doses:
            if parameter is None or not (parameter >= 0):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)

        _card.Card.__init__(self, f'embde{suffix}')
        self.mnemonic = DatumMnemonic.EMBEDDED_DOSE_BOUNDARIES
        self.parameters = doses
        self.suffix = suffix

        self.doses = doses
