import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Lca(DataOption):
    """
    Represents INP lca elements.

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

    _ATTRS = {
        'ielas': types.IntegerOrJump,
        'ipreg': types.IntegerOrJump,
        'iexisa': types.IntegerOrJump,
        'ichoic': types.IntegerOrJump,
        'jcoul': types.IntegerOrJump,
        'nexite': types.IntegerOrJump,
        'npidk': types.IntegerOrJump,
        'noact': types.IntegerOrJump,
        'icem': types.IntegerOrJump,
        'ilaq': types.IntegerOrJump,
        'nevtype': types.IntegerOrJump,
    }

    _REGEX = re.compile(
        rf'\Alca( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        ielas: types.IntegerOrJump,
        ipreg: types.IntegerOrJump,
        iexisa: types.IntegerOrJump,
        ichoic: types.IntegerOrJump,
        jcoul: types.IntegerOrJump,
        nexite: types.IntegerOrJump,
        npidk: types.IntegerOrJump,
        noact: types.IntegerOrJump,
        icem: types.IntegerOrJump,
        ilaq: types.IntegerOrJump,
        nevtype: types.IntegerOrJump,
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
            InpError: SEMANTICS_OPTION.
        """

        if ielas is None or not (ielas == 0 or ielas == 1 or ielas == 2):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ielas)
        if ipreg is None or not (ipreg == 0 or ipreg == 1 or ipreg == 2 or ipreg == 3):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ipreg)
        if iexisa is None or not (iexisa == 0 or iexisa == 1 or iexisa == 2):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, iexisa)
        if ichoic is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ichoic)
        if jcoul is None or not (jcoul == 0 or jcoul == 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, jcoul)
        if nexite is None or not (nexite == 0 or nexite == 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, nexite)
        if npidk is None or not (npidk == 0 or npidk == 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, npidk)
        if noact is None or not (
            noact == -2 or noact == -1 or noact == 0 or noact == 1 or noact == 2
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, noact)
        if icem is None or not (icem == 0 or icem == 1 or icem == 2):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, icem)
        if ilaq is None or not (ilaq == 0 or ilaq == 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ilaq)
        if nevtype is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, nevtype)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                ielas,
                ipreg,
                iexisa,
                ichoic,
                jcoul,
                nexite,
                npidk,
                noact,
                icem,
                ilaq,
                nevtype,
            ]
        )

        self.ielas: typing.Final[types.IntegerOrJump] = ielas
        self.ipreg: typing.Final[types.IntegerOrJump] = ipreg
        self.iexisa: typing.Final[types.IntegerOrJump] = iexisa
        self.ichoic: typing.Final[types.IntegerOrJump] = ichoic
        self.jcoul: typing.Final[types.IntegerOrJump] = jcoul
        self.nexite: typing.Final[types.IntegerOrJump] = nexite
        self.npidk: typing.Final[types.IntegerOrJump] = npidk
        self.noact: typing.Final[types.IntegerOrJump] = noact
        self.icem: typing.Final[types.IntegerOrJump] = icem
        self.ilaq: typing.Final[types.IntegerOrJump] = ilaq
        self.nevtype: typing.Final[types.IntegerOrJump] = nevtype


@dataclasses.dataclass
class LcaBuilder:
    """
    Builds ``Lca``.

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

    ielas: str | int | types.IntegerOrJump
    ipreg: str | int | types.IntegerOrJump
    iexisa: str | int | types.IntegerOrJump
    ichoic: str | int | types.IntegerOrJump
    jcoul: str | int | types.IntegerOrJump
    nexite: str | int | types.IntegerOrJump
    npidk: str | int | types.IntegerOrJump
    noact: str | int | types.IntegerOrJump
    icem: str | int | types.IntegerOrJump
    ilaq: str | int | types.IntegerOrJump
    nevtype: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``LcaBuilder`` into ``Lca``.

        Returns:
            ``Lca`` for ``LcaBuilder``.
        """

        if isinstance(self.ielas, types.Integer):
            ielas = self.ielas
        elif isinstance(self.ielas, int):
            ielas = types.IntegerOrJump(self.ielas)
        elif isinstance(self.ielas, str):
            ielas = types.IntegerOrJump.from_mcnp(self.ielas)

        if isinstance(self.ipreg, types.Integer):
            ipreg = self.ipreg
        elif isinstance(self.ipreg, int):
            ipreg = types.IntegerOrJump(self.ipreg)
        elif isinstance(self.ipreg, str):
            ipreg = types.IntegerOrJump.from_mcnp(self.ipreg)

        if isinstance(self.iexisa, types.Integer):
            iexisa = self.iexisa
        elif isinstance(self.iexisa, int):
            iexisa = types.IntegerOrJump(self.iexisa)
        elif isinstance(self.iexisa, str):
            iexisa = types.IntegerOrJump.from_mcnp(self.iexisa)

        if isinstance(self.ichoic, types.Integer):
            ichoic = self.ichoic
        elif isinstance(self.ichoic, int):
            ichoic = types.IntegerOrJump(self.ichoic)
        elif isinstance(self.ichoic, str):
            ichoic = types.IntegerOrJump.from_mcnp(self.ichoic)

        if isinstance(self.jcoul, types.Integer):
            jcoul = self.jcoul
        elif isinstance(self.jcoul, int):
            jcoul = types.IntegerOrJump(self.jcoul)
        elif isinstance(self.jcoul, str):
            jcoul = types.IntegerOrJump.from_mcnp(self.jcoul)

        if isinstance(self.nexite, types.Integer):
            nexite = self.nexite
        elif isinstance(self.nexite, int):
            nexite = types.IntegerOrJump(self.nexite)
        elif isinstance(self.nexite, str):
            nexite = types.IntegerOrJump.from_mcnp(self.nexite)

        if isinstance(self.npidk, types.Integer):
            npidk = self.npidk
        elif isinstance(self.npidk, int):
            npidk = types.IntegerOrJump(self.npidk)
        elif isinstance(self.npidk, str):
            npidk = types.IntegerOrJump.from_mcnp(self.npidk)

        if isinstance(self.noact, types.Integer):
            noact = self.noact
        elif isinstance(self.noact, int):
            noact = types.IntegerOrJump(self.noact)
        elif isinstance(self.noact, str):
            noact = types.IntegerOrJump.from_mcnp(self.noact)

        if isinstance(self.icem, types.Integer):
            icem = self.icem
        elif isinstance(self.icem, int):
            icem = types.IntegerOrJump(self.icem)
        elif isinstance(self.icem, str):
            icem = types.IntegerOrJump.from_mcnp(self.icem)

        if isinstance(self.ilaq, types.Integer):
            ilaq = self.ilaq
        elif isinstance(self.ilaq, int):
            ilaq = types.IntegerOrJump(self.ilaq)
        elif isinstance(self.ilaq, str):
            ilaq = types.IntegerOrJump.from_mcnp(self.ilaq)

        if isinstance(self.nevtype, types.Integer):
            nevtype = self.nevtype
        elif isinstance(self.nevtype, int):
            nevtype = types.IntegerOrJump(self.nevtype)
        elif isinstance(self.nevtype, str):
            nevtype = types.IntegerOrJump.from_mcnp(self.nevtype)

        return Lca(
            ielas=ielas,
            ipreg=ipreg,
            iexisa=iexisa,
            ichoic=ichoic,
            jcoul=jcoul,
            nexite=nexite,
            npidk=npidk,
            noact=noact,
            icem=icem,
            ilaq=ilaq,
            nevtype=nevtype,
        )
