import re

from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors


class Lca(Datum):
    """
    ``Lca`` represents INP model physics LCA data cards.

    ``Lca`` inherits attributes from ``Datum``. It represents the INP model
    physics LCA data card syntax element.

    Attributes:
        ielas: Elastic scattering controls.
        ipreq: Pre-equilibrium model controls.
        iexisa: Model choice controls.
        ichoic: ISABEL intranuclear cascade modifier controls.
        jcoul: Coulomb barrier for incident charged particles controls.
        nexite: Nuclear recoil energy to get excitation energy.
        npidk: Pion interaction control.
        noact: Particle transport options.
        icem: Choose alternative physics model.
        ilaq: Choose light ion and nucleon physics modules.
        nevtype: Choose number of evaporation particles modeled by GEM2.
    """

    def __init__(
        self,
        ielas: types.McnpInteger,
        ipreq: types.McnpInteger,
        iexisa: types.McnpInteger,
        ichoic: str,
        jcoul: types.McnpInteger,
        nexite: types.McnpInteger,
        npidk: types.McnpInteger,
        noact: types.McnpInteger,
        icem: types.McnpInteger,
        ilaq: types.McnpInteger,
        nevtype: types.McnpReal,
    ):
        """
        ``__init__`` initializes ``Lca``.

        Parameters:
            ielas: Elastic scattering controls.
            ipreq: Pre-equilibrium model controls.
            iexisa: Model choice controls.
            ichoic: ISABEL intranuclear cascade modifier controls.
            jcoul: Coulomb barrier for incident charged particles controls.
            nexite: Nuclear recoil energy to get excitation energy.
            npidk: Pion interaction control.
            noact: Particle transport options.
            icem: Choose alternative physics model.
            ilaq: Choose light ion and nucleon physics modules.
            nevtype: Choose number of evaporation particles modeled by GEM2.
        """

        if ielas is None or ielas not in {0, 1, 2}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ipreq is None or ipreq not in {0, 1, 2, 3}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if iexisa is None or iexisa not in {0, 1, 2}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ichoic is None or not (re.match(r'(0|1|-2)([0-9])([0-5])([1-6])'.ichoic)):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if jcoul is None or jcoul not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if nexite is None or nexite not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if npidk is None or npidk not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if noact is None or noact not in {-2, -1, 0, 1, 2}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if icem is None or icem not in {0, 1, 2}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ilaq is None or ilaq not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if nevtype is None or not (nevtype >= 0):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, 'lca')
        self.mnemonic = DatumMnemonic.LCA
        self.parameters = (
            ielas,
            ipreq,
            iexisa,
            ichoic,
            jcoul,
            nexite,
            npidk,
            noact,
            icem,
            ilaq,
            nevtype,
        )

        self.ielas = ielas
        self.ipreq = ipreq
        self.iexisa = iexisa
        self.ichoic = ichoic
        self.jcoul = jcoul
        self.nexite = nexite
        self.npidk = npidk
        self.noact = noact
        self.icem = icem
        self.ilaq = ilaq
        self.nevtype = nevtype
