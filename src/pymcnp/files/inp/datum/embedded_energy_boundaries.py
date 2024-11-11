from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors


class EmbeddedEnergyBoundaries(Datum):
    """
    ``EmbeddedEnergyBoundaries`` represents INP embedded elemental
    edits energy boundaries.

    ``EmbeddedEnergyBoundaries`` inherits attributes from ``Datum``. It
    represents the INP embedded embedded elemental edits energy boundaries data
    card syntax element.

    Attributes:
        energies: Tuple of energy lower bounds.
        suffix: Data card suffix.
    """

    def __init__(self, energies: tuple[float], suffix: types.McnpInteger):
        """
        ``__init__`` initializes ``EmbeddedEnergyBoundaries``.

        Parameters:
            energies: Tuple of energy lower bounds.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
            MCNPSemanticError: INVALID_DATUM_SUFFIX.
        """

        for parameter in energies:
            if parameter is None or not (parameter >= 0):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)

        _card.Card.__init__(self, f'embeb{suffix}')
        self.mnemonic = DatumMnemonic.EMBEDDED_ENERGY_BOUNDARIES
        self.parameters = energies
        self.suffix = suffix

        self.energies = energies
