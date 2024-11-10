from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors


class Lcb(Datum):
    """
    ``Lcb`` represents INP model physics LCB data cards.

    ``Lcb`` inherits attributes from ``Datum``. It represents the INP model
    physics LCB data card syntax element.

    Attributes:
        flebn1: Kinetic energy #1.
        flebn2: Kinetic energy #2.
        flebn3: Kinetic energy #3.
        flebn4: Kinetic energy #4.
        flebn5: Kinetic energy #5.
        flebn6: Kinetic energy #6.
        ctofe: Cutoff kinetic energy.
        flim0: Maximum correction allowed for mass-energy balacing.
    """

    def __init__(
        self,
        flebn1: types.McnpReal,
        flebn2: types.McnpReal,
        flebn3: types.McnpReal,
        flebn4: types.McnpReal,
        flebn5: types.McnpReal,
        flebn6: types.McnpReal,
        ctofe: types.McnpReal,
        flim0: types.McnpReal,
    ):
        """
        ``__init__`` initializes ``Lcb``.

        Parameters:
            flebn1: Kinetic energy #1.
            flebn2: Kinetic energy #2.
            flebn3: Kinetic energy #3.
            flebn4: Kinetic energy #4.
            flebn5: Kinetic energy #5.
            flebn6: Kinetic energy #6.
            ctofe: Cutoff kinetic energy.
            flim0: Maximum correction allowed for mass-energy balacing.
        """

        if flebn1 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if flebn2 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if flebn3 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if flebn4 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if flebn5 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if flebn6 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ctofe is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if flim0 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, 'lcb')
        self.mnemonic = DatumMnemonic.LCB
        self.parameters = (flebn1, flebn2, flebn3, flebn4, flebn5, flebn6, ctofe, flim0)

        self.flebn1 = flebn1
        self.flebn2 = flebn2
        self.flebn3 = flebn3
        self.flebn4 = flebn4
        self.flebn5 = flebn5
        self.flebn6 = flebn6
        self.ctofe = ctofe
        self.flim0 = flim0
