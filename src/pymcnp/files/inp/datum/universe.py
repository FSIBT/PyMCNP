from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import errors


class Universe(Datum):
    """
    ``Universe`` represents INP universe data cards.

    ``Universe`` inherits attributes from ``Datum``. It represents the INP
    universe data card syntax element.

    Attributes:
        universes: Tuple of cell universe numbers.
    """

    def __init__(self, universes: tuple[int]):
        """
        ``__init__`` initializes ``Universe``.

        Parameters:
            universes: Tuple of cell universe numbers.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in universes:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, 'u')
        self.mnemonic = DatumMnemonic.UNIVERSE
        self.universes = universes

        self.parameters = universes
