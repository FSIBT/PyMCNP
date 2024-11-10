from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors


class Lea(Datum):
    """
    ``Lea`` represents INP model physics LEA data cards.

    ``Lea`` inherits attributes from ``Datum``. It represents the INP model
    physics LEA data card syntax element.

    Attributes:
        ipht: Generation of de-excitation phontes controls.
        icc: Level of physics for PHT physics definitions.
        nobalc: Mass-energy balancing in cascade controls.
        nobale: Mass-energy balancing in evaporation controls.
        ifbrk: Fermi-breakup model nuclide range controls.
        ilvden: Level-density model controls.
        ievap: Evaporation and fission models controls.
        nofis: Fission controls.
    """

    def __init__(
        self,
        ipht: types.McnpInteger,
        icc: types.McnpInteger,
        nobalc: types.McnpInteger,
        nobale: types.McnpInteger,
        ifbrk: types.McnpInteger,
        ilvden: types.McnpInteger,
        ievap: types.McnpInteger,
        nofis: types.McnpInteger,
    ):
        """
        ``__init__`` initializes ``Lea``.

        Parameters:
            ipht: Generation of de-excitation phontes controls.
            icc: Level of physics for PHT physics definitions.
            nobalc: Mass-energy balancing in cascade controls.
            nobale: Mass-energy balancing in evaporation controls.
            ifbrk: Fermi-breakup model nuclide range controls.
            ilvden: Level-density model controls.
            ievap: Evaporation and fission models controls.
            nofis: Fission controls.
        """

        if ipht is None or ipht not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if icc is None or icc not in {0, 1, 2, 3, 4}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if nobalc is None or nobalc not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if nobale is None or nobale not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ifbrk is None or ifbrk not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ilvden is None or ilvden not in {-1, 0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ievap is None or ievap not in {0, -1, 1, 2}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if nofis is None or nofis not in {1, 0}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, 'lea')
        self.mnemonic = DatumMnemonic.LEA
        self.parameters = (ipht, icc, nobalc, nobale, ifbrk, ilvden, ievap, nofis)

        self.ipht = ipht
        self.icc = icc
        self.nobalc = nobalc
        self.nobale = nobale
        self.ifbrk = ifbrk
        self.ilvden = ilvden
        self.ievap = ievap
        self.nofis = nofis
