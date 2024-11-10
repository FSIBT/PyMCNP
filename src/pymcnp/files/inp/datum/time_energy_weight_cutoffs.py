from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors


class TimeEnergyWeightCutoffs(Datum):
    """
    ``TimeEnergyWeightCutoffs`` represents INP time, energy, and weight cutoffs
    data cards.

    ``TimeEnergyWeightCutoffs`` inherits attributes from ``Datum``. It
    represents the INP time, energy, and weight cutoffs data card syntax
    element.

    Attributes:
        designator: Particle designator.
        time: Time cutoff.
        energy: Lower energy cutoff.
        weight1: Weight cutoff #1.
        weight2: Weight cutoff #2.
        source: Minimum source weight.
    """

    def __init__(
        self,
        designator: types.Designator,
        time: types.McnpReal,
        energy: types.McnpReal,
        weight1: types.McnpReal,
        weight2: types.McnpReal,
        source: types.McnpReal,
    ):
        """
        ``__init__`` initializes ``TimeEnergyWeightCutoffs``.

        Parameters:
            designator: Particle designator.
            time: Time cutoff.
            energy: Lower energy cutoff.
            weight1: Weight cutoff #1.
            weight2: Weight cutoff #2.
            source: Minimum source weight.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DESIGNATOR.
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        if designator is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DESIGNATOR)

        if time is None or not (time == 'j' or time > 0):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        # if energy is None or not (energy == 'j' or energy > 0):
        # raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        # if weight1 is None:
        # raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        # if weight2 is None:
        # raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        # if source is None:
        # raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, f'cut:{designator.to_mcnp()}')
        self.mnemonic = DatumMnemonic.TIME_ENERGY_WEIGHT_CUTOFFS
        self.parameters = (time, energy, weight1, weight2, source)
        self.designator = designator

        self.time = time
        self.energy = energy
        self.weight1 = weight1
        self.weight2 = weight2
        self.source = source
