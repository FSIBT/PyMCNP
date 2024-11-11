from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors


class DiscreteReactionCrossSection(Datum):
    """
    ``DiscreteReactionCrossSection`` represents INP discrete-reaction cross
    section data cards.

    ``DiscreteReactionCrossSection`` inherits attributes from ``Datum``. It
    represents the INP discrete-reaction cross section data card syntax
    element.

    Attributes:
        zaids: Tuple of ZAID specifiers.
    """

    def __init__(self, zaids: tuple[types.Zaid]):
        """
        ``__init__`` initializes ``DiscreteReactionCrossSection``.

        Parameters:
            zaids: Tuple of ZAID specifiers.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for zaid in zaids:
            if zaid is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, 'drxs')
        self.mnemonic = DatumMnemonic.DISCRETE_REACTIONC_CROSS_SECTION
        self.parameters = zaids

        self.zaids = zaids
