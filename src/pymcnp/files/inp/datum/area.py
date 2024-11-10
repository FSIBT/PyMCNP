from typing import Final

from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import errors


class Area(Datum):
    """
    ``Area`` represents INP area data cards.

    ``Area`` inherits attributes from ``Datum``. It represents the INP area
    data card syntax element.

    Attributes:
        areas: Tuple of cell areas.
    """

    def __init__(self, areas: tuple[float]):
        """
        ``__init__`` initializes ``Area``.

        Parameters:
            areas: Tuple of cell areas.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in areas:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, 'area')
        self.mnemonic: Final[DatumMnemonic] = DatumMnemonic.AREA
        self.parameters: Final[tuple[float]] = areas

        self.areas: Final[tuple[float]] = areas
