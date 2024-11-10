from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import errors


class Fill(Datum):
    """
    ``Fill`` represents INP fill data cards.

    ``Fill`` inherits attributes from ``Datum``. It represents the INP
    universe data card syntax element.

    Attributes:
        fills: Tuple of universe numbers.
        is_angle: Angle unit setting.
    """

    def __init__(self, fills: tuple[int], is_angle: bool = False):
        """
        ``__init__`` initializes ``Fill``.

        Parameters:
            fills: Tuple of universe numbers.
            is_angle: Angle unit setting.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in fills:
            if parameter is None or not (parameter >= 0 and parameter <= 99_999_999):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, 'fill')
        self.mnemonic = DatumMnemonic.FILL
        self.parameters = fills

        self.fills = fills
        self.is_angle = is_angle
