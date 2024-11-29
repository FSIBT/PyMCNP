"""
Contains the ``Lca`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ...utils import types, errors, _parser


class Lca(Data):
    """
    Represents INP lca data cards.

    ``Lca`` implements ``Data``.

    Attributes:
        ielas: Elastic scattering controls.
        ipreg: pre-equilibrium model.
        iexisa: Model choice controls.
        ichoic: ISABEL intranuclear cascade model control.
        jcoul: Coulomb barrier for incident charged particle controls.
        nexite: Subtract nuclear recoil energy to get excitation energy.
        npidk: Cutoff interact/terminate control.
        noact: Particle transport settings.
        icem: Choose alternative physics model.
        ilaq: Choose light ion and nucleon physics modules.
        nevtype: Choose number of evaporation particles for GEM2.
    """

    def __init__(
        self,
        ielas: types.McnpInteger,
        ipreg: types.McnpInteger,
        iexisa: types.McnpInteger,
        ichoic: types.McnpInteger,
        jcoul: types.McnpInteger,
        nexite: types.McnpInteger,
        npidk: types.McnpInteger,
        noact: types.McnpInteger,
        icem: types.McnpInteger,
        ilaq: types.McnpInteger,
        nevtype: types.McnpInteger,
    ):
        """
        Initializes ``Lca``.

        Parameters:
            ielas: Elastic scattering controls.
            ipreg: pre-equilibrium model.
            iexisa: Model choice controls.
            ichoic: ISABEL intranuclear cascade model control.
            jcoul: Coulomb barrier for incident charged particle controls.
            nexite: Subtract nuclear recoil energy to get excitation energy.
            npidk: Cutoff interact/terminate control.
            noact: Particle transport settings.
            icem: Choose alternative physics model.
            ilaq: Choose light ion and nucleon physics modules.
            nevtype: Choose number of evaporation particles for GEM2.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if ielas is None or not (ielas == 0 or ielas == 1 or ielas == 2):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(ielas))

        if ipreg is None or not (ipreg == 0 or ipreg == 1 or ipreg == 2 or ipreg == 3):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(ipreg))

        if iexisa is None or not (iexisa == 0 or iexisa == 1 or iexisa == 2):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(iexisa))

        if ichoic is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(ichoic))

        if jcoul is None or not (jcoul == 0 or jcoul == 1):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(jcoul))

        if nexite is None or not (nexite == 0 or nexite == 1):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(nexite))

        if npidk is None or not (npidk == 0 or npidk == 1):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(npidk))

        if noact is None or not (
            noact == -2 or noact == -1 or noact == 0 or noact == 1 or noact == 2
        ):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(noact))

        if icem is None or not (icem == 0 or icem == 1 or icem == 2):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(icem))

        if ilaq is None or not (ilaq == 0 or ilaq == 1):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(ilaq))

        if nevtype is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(nevtype))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.LCA
        self.parameters: Final[tuple[any]] = tuple(
            [ielas]
            + [ipreg]
            + [iexisa]
            + [ichoic]
            + [jcoul]
            + [nexite]
            + [npidk]
            + [noact]
            + [icem]
            + [ilaq]
            + [nevtype]
        )
        self.ielas: Final[types.McnpInteger] = ielas
        self.ipreg: Final[types.McnpInteger] = ipreg
        self.iexisa: Final[types.McnpInteger] = iexisa
        self.ichoic: Final[types.McnpInteger] = ichoic
        self.jcoul: Final[types.McnpInteger] = jcoul
        self.nexite: Final[types.McnpInteger] = nexite
        self.npidk: Final[types.McnpInteger] = npidk
        self.noact: Final[types.McnpInteger] = noact
        self.icem: Final[types.McnpInteger] = icem
        self.ilaq: Final[types.McnpInteger] = ilaq
        self.nevtype: Final[types.McnpInteger] = nevtype
        self.ident: Final[str] = 'lca'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Lca`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for lca data cards.

        Returns:
            ``Lca`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN, KEYWORD_DATUM_MNEMONIC.
        """

        source = _parser.Preprocessor.process_inp(source)
        source, comments = _parser.Preprocessor.process_inp_comments(source)
        tokens = _parser.Parser(
            re.split(r' |:|=', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        mnemonic = re.search(r'^[a-zA-Z*]+', tokens.peekl())
        mnemonic = mnemonic[0] if mnemonic else ''
        if mnemonic != 'lca':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        ielas = types.McnpInteger.from_mcnp(tokens.popl())
        ipreg = types.McnpInteger.from_mcnp(tokens.popl())
        iexisa = types.McnpInteger.from_mcnp(tokens.popl())
        ichoic = types.McnpInteger.from_mcnp(tokens.popl())
        jcoul = types.McnpInteger.from_mcnp(tokens.popl())
        nexite = types.McnpInteger.from_mcnp(tokens.popl())
        npidk = types.McnpInteger.from_mcnp(tokens.popl())
        noact = types.McnpInteger.from_mcnp(tokens.popl())
        icem = types.McnpInteger.from_mcnp(tokens.popl())
        ilaq = types.McnpInteger.from_mcnp(tokens.popl())
        nevtype = types.McnpInteger.from_mcnp(tokens.popl())

        data = Lca(ielas, ipreg, iexisa, ichoic, jcoul, nexite, npidk, noact, icem, ilaq, nevtype)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Lca`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Lca``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f'{self.mnemonic.to_mcnp()} {self.ielas.to_mcnp()} {self.ipreg.to_mcnp()} {self.iexisa.to_mcnp()} {self.ichoic.to_mcnp()} {self.jcoul.to_mcnp()} {self.nexite.to_mcnp()} {self.npidk.to_mcnp()} {self.noact.to_mcnp()} {self.icem.to_mcnp()} {self.ilaq.to_mcnp()} {self.nevtype.to_mcnp()}'
        )
