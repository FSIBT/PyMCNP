from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import errors


class TotalFission(Datum):
    """
    ``OnTheFlyBroadening`` represents INP total fission data cards.

    ``OnTheFlyBroadening`` inherits attributes from ``Datum``. It represents
    the INP on-the-fly boradening data card syntax element.

    Attributes:
        has_no: No volume calculation option.
    """

    def __init__(self, has_no: bool):
        """
        ``__init__`` initializes ``TotalFission``.

        Parameters:
           has_no: No volume calculation option.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        if has_no is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, 'totnu')
        self.mnemonic = DatumMnemonic.TOTAL_FISSION
        self.parameters = (has_no,)

        self.states = has_no
