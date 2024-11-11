from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors


class FissionTurnoff(Datum):
    """
    ``FissionTurnoff`` represents INP fission turnoff data cards.

    ``FissionTurnoff`` inherits attributes from ``Datum``. It represents
    the INP fission turnoff data card syntax element.

    Attributes:
        states: Tuple of fission turnoff settings.
    """

    def __init__(self, states: types.McnpInteger):
        """
        ``__init__`` initializes ``FissionTurnoff``.

        Parameters:
            states: Tuple of fission turnoff settings.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in states:
            if parameter is None or parameter not in {0, 1, 2}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, 'nonu')
        self.mnemonic = DatumMnemonic.FISSION_TURNOFF
        self.parameters = states

        self.states = states
