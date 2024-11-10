from typing import Final

from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors


class HistoryCutoff(Datum):
    """
    ``HistoryCutoff`` represents INP nps data cards.

    ``HistoryCutoff`` inherits attributes from ``Datum``. It represents the INP
    nps data card syntax element.

    Attributes:
        npp: Total number of histories to run.
        npsmg: Number of history with direct source contributions.
    """

    def __init__(self, npp: types.McnpInteger, npsmg: types.McnpInteger):
        """
        ``__init__`` initializes ``HistoryCutoff``.

        Parameters:
            npp: Total number of histories to run.
            npsmg: Number of history with direct source contributions.
        """

        if npp is None or not (npp > 0):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        # if npsmg is None or not (npsmg > 0):
        # raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, 'nps')
        self.mnemonic: Final[DatumMnemonic] = DatumMnemonic.HISTORY_CUTOFF
        self.parameters: Final[tuple] = (npp, npsmg)

        self.npp: Final[int] = npp
        self.npsmg: Final[int] = npsmg
