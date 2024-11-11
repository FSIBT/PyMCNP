from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import errors


class Lattice(Datum):
    """
    ``Lattice`` represents INP lattice data cards.

    ``Lattice`` inherits attributes from ``Datum``. It represents the INP
    lattice data card syntax element.

    Attributes:
        lattices: Tuple of cell lattice numbers.
    """

    def __init__(self, lattices: tuple[int]):
        """
        ``__init__`` initializes ``Lattice``.

        Parameters:
            lattices: Tuple of cell lattice numbers.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in lattices:
            if parameter is None or parameter not in {1, 2}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, 'lat')
        self.mnemonic = DatumMnemonic.LATTICE
        self.lattices = lattices

        self.parameters = lattices
