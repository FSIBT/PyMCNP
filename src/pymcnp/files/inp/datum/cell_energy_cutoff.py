from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors


class CellEnergyCutoff(Datum):
    """
    ``CellEnergyCutoff`` represents INP cell-by-cell energy cutoffs data cards.

    ``CellEnergyCutoff`` inherits attributes from ``Datum``. It represents the
    INP cell-by-cell energy cutoffs data card syntax element.

    Attributes:
        designator: Particle designator.
        cutoffs: Lower energy cutoff of cells.
    """

    def __init__(self, designator: types.Designator, cutoffs: tuple[float]):
        """
        ``__init__`` initializes ``CellEnergyCutoff``.

        Parameters:
            designator: Particle designator.
            cutoffs: Lower energy cutoff of cells.
        """

        if designator is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DESIGNATOR)

        if cutoffs is None or not cutoffs:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        for cutoff in cutoffs:
            if cutoff is None or not (cutoff > 0):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, f'elpt:{designator.to_mcnp()}')
        self.mnemonic = DatumMnemonic.CELL_ENERGY_CUTOFF
        self.parameters = cutoffs
        self.designator = designator

        self.cutoffs = cutoffs
