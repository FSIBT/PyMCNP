from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors


class EmbeddedTimeBoundaries(Datum):
    """
    ``EmbeddedTimeBoundaries`` represents INP embedded elemental edits
    time boundaries.

    ``EmbeddedTimeBoundaries`` inherits attributes from ``Datum``. It
    represents the INP embedded embedded elemental edits time boundaries data
    card syntax element.

    Attributes:
        times: Tuple of time lower bounds.
    """

    def __init__(self, times: tuple[float], suffix: types.McnpInteger):
        """
        ``__init__`` initializes ``EmbeddedTimeBoundaries``.

        Parameters:
            times: Tuple of time lower bounds.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
            MCNPSemanticError: INVALID_DATUM_SUFFIX
        """

        for parameter in times:
            if parameter is None or not (parameter >= 0):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)

        _card.Card.__init__(self, f'embtb{suffix}')
        self.mnemonic = DatumMnemonic.EMBEDDED_TIME_BOUNDARIES
        self.parameters = times
        self.suffix = suffix

        self.times = times
