from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors


class Lcc(Datum):
    """
    ``Lcc`` represents INP model physics LCC data cards.

    ``Lcc`` inherits attributes from ``Datum``. It represents the INP model
    physics LCC data card syntax element.

    Attributes:
        atincl: Rescaling factor of the cascade duration.
        v0incl: Potential depth.
        xfoisaincl: Maximum impact parameter for Pauli blokcing controls.
        npaulincl: Pauli blocking parameter.
        nosurfincl: Diffuse nuclear surface based on density controls.
        ecutincl: Use Bertini model below this energy.
        ebankincl: Wrtie no INCL bank particles.
        ebankabla: Write not ABLA bank particles.
    """

    def __init__(
        self,
        atincl: types.McnpReal,
        v0incl: types.McnpReal,
        xfoisaincl: types.McnpReal,
        npaulincl: types.McnpInteger,
        nosurfincl: types.McnpInteger,
        ecutincl: types.McnpReal,
        ebankincl: types.McnpReal,
        ebankabla: types.McnpReal,
    ):
        """
        ``__init__`` initializes ``Lcc``.

        Parameters:
            atincl: Rescaling factor of the cascade duration.
            v0incl: Potential depth.
            xfoisaincl: Maximum impact parameter for Pauli blokcing controls.
            npaulincl: Pauli blocking parameter.
            nosurfincl: Diffuse nuclear surface based on density controls.
            ecutincl: Use Bertini model below this energy.
            ebankincl: Wrtie no INCL bank particles.
            ebankabla: Write not ABLA bank particles.
        """

        if atincl is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if v0incl is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if xfoisaincl is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if npaulincl is None or npaulincl not in {1, 0, -1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if nosurfincl is None or nosurfincl not in {-2, -1, 0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ecutincl is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ebankincl is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ebankabla is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, 'lcc')
        self.mnemonic = DatumMnemonic.LCB
        self.parameters = (
            atincl,
            v0incl,
            xfoisaincl,
            npaulincl,
            nosurfincl,
            ecutincl,
            ebankincl,
            ebankabla,
        )

        self.atincl = atincl
        self.v0incl = v0incl
        self.xfoisaincl = xfoisaincl
        self.npaulincl = npaulincl
        self.nosurfincl = nosurfincl
        self.ecutincl = ecutincl
        self.ebankincl = ebankincl
        self.ebankabla = ebankabla
