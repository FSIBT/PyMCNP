from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import errors


class Void(Datum):
    """
    ``Void`` represents INP material void data cards.

    ``Void`` inherits attributes from ``Datum``. It represents the INP material
    void data card syntax element.

    Attributes:
        numbers: Tuple of cell numbers.
    """

    def __init__(self, numbers: tuple[int]):
        """
        ``__init__`` initializes ``Void``.

        Parameters:
            numbers: Tuple of cell numbers.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in numbers:
            if parameter is None or not (1 <= parameter <= 99_999_999):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, 'void')
        self.mnemonic = DatumMnemonic.VOID
        self.parameters = numbers

        self.numbers = numbers
