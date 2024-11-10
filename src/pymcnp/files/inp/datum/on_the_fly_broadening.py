from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors


class OnTheFlyBroadening(Datum):
    """
    ``OnTheFlyBroadening`` represents INP on-the-fly broadening data cards.

    ``OnTheFlyBroadening`` inherits attributes from ``Datum``. It represents
    the INP on-the-fly boradening data card syntax element.

    Attributes:
        zaids: Tuple of ZAID alias.
    """

    def __init__(self, zaids: tuple[types.Zaid]):
        """
        ``__init__`` initializes ``OnTheFlyBroadening``.

        Parameters:
            zaids: Tuple of ZAID alias.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in zaids:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, 'otfdb')
        self.mnemonic = DatumMnemonic.ONTHEFLY_BROADENING
        self.parameters = zaids

        self.zaids = zaids
