from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors


class ProblemType(Datum):
    """
    ``ProblemType`` represents INP problem type data cards.

    ``ProblemType`` inherits attributes from ``Datum``. It represents the INP
    problem type data card syntax element.

    Attributes:
        particles: Tuple of particle designators.
    """

    def __init__(self, particles: tuple[types.Designator]):
        """
        ``__init__`` initializes ``DiscreteReactionCrossSection``.

        Parameters:
            particles: Tuple of particle designators.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        if particles is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        for particle in particles:
            if particle is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, 'mode')
        self.mnemonic = DatumMnemonic.PROBLEM_TYPE
        self.parameters = particles

        self.particles = particles
