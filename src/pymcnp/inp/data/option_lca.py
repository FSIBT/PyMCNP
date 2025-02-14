import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Lca(_option.DataOption_, keyword='lca'):
    """
    Represents INP data card lca options.

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

    _REGEX = re.compile(
        r'\Alca( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)\Z'
    )

    def __init__(
        self,
        ielas: types.Integer,
        ipreg: types.Integer,
        iexisa: types.Integer,
        ichoic: types.Integer,
        jcoul: types.Integer,
        nexite: types.Integer,
        npidk: types.Integer,
        noact: types.Integer,
        icem: types.Integer,
        ilaq: types.Integer,
        nevtype: types.Integer,
    ):
        """
        Initializes ``DataOption_Lca``.

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

        Returns:
            ``DataOption_Lca``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if ielas is None or not (ielas == 0 or ielas == 1 or ielas == 2):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, ielas)
        if ipreg is None or not (ipreg == 0 or ipreg == 1 or ipreg == 2 or ipreg == 3):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, ipreg)
        if iexisa is None or not (iexisa == 0 or iexisa == 1 or iexisa == 2):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, iexisa)
        if ichoic is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, ichoic)
        if jcoul is None or not (jcoul == 0 or jcoul == 1):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, jcoul)
        if nexite is None or not (nexite == 0 or nexite == 1):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, nexite)
        if npidk is None or not (npidk == 0 or npidk == 1):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, npidk)
        if noact is None or not (
            noact == -2 or noact == -1 or noact == 0 or noact == 1 or noact == 2
        ):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, noact)
        if icem is None or not (icem == 0 or icem == 1 or icem == 2):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, icem)
        if ilaq is None or not (ilaq == 0 or ilaq == 1):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, ilaq)
        if nevtype is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, nevtype)

        self.value: typing.Final[tuple[any]] = types._Tuple(
            [ielas, ipreg, iexisa, ichoic, jcoul, nexite, npidk, noact, icem, ilaq, nevtype]
        )
        self.ielas: typing.Final[types.Integer] = ielas
        self.ipreg: typing.Final[types.Integer] = ipreg
        self.iexisa: typing.Final[types.Integer] = iexisa
        self.ichoic: typing.Final[types.Integer] = ichoic
        self.jcoul: typing.Final[types.Integer] = jcoul
        self.nexite: typing.Final[types.Integer] = nexite
        self.npidk: typing.Final[types.Integer] = npidk
        self.noact: typing.Final[types.Integer] = noact
        self.icem: typing.Final[types.Integer] = icem
        self.ilaq: typing.Final[types.Integer] = ilaq
        self.nevtype: typing.Final[types.Integer] = nevtype

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Lca`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Lca``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Lca._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        ielas = types.Integer.from_mcnp(tokens[1])
        ipreg = types.Integer.from_mcnp(tokens[2])
        iexisa = types.Integer.from_mcnp(tokens[3])
        ichoic = types.Integer.from_mcnp(tokens[4])
        jcoul = types.Integer.from_mcnp(tokens[5])
        nexite = types.Integer.from_mcnp(tokens[6])
        npidk = types.Integer.from_mcnp(tokens[7])
        noact = types.Integer.from_mcnp(tokens[8])
        icem = types.Integer.from_mcnp(tokens[9])
        ilaq = types.Integer.from_mcnp(tokens[10])
        nevtype = types.Integer.from_mcnp(tokens[11])

        return DataOption_Lca(
            ielas, ipreg, iexisa, ichoic, jcoul, nexite, npidk, noact, icem, ilaq, nevtype
        )
