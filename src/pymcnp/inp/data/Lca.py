import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Lca(_option.DataOption):
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

    _KEYWORD = 'lca'

    _ATTRS = {
        'ielas': types.Integer,
        'ipreg': types.Integer,
        'iexisa': types.Integer,
        'ichoic': types.Integer,
        'jcoul': types.Integer,
        'nexite': types.Integer,
        'npidk': types.Integer,
        'noact': types.Integer,
        'icem': types.Integer,
        'ilaq': types.Integer,
        'nevtype': types.Integer,
    }

    _REGEX = re.compile(
        rf'\Alca( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?\Z'
    )

    def __init__(
        self,
        ielas: types.Integer = None,
        ipreg: types.Integer = None,
        iexisa: types.Integer = None,
        ichoic: types.Integer = None,
        jcoul: types.Integer = None,
        nexite: types.Integer = None,
        npidk: types.Integer = None,
        noact: types.Integer = None,
        icem: types.Integer = None,
        ilaq: types.Integer = None,
        nevtype: types.Integer = None,
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

        if ielas is not None and not (isinstance(ielas.value, types.Jump) or ielas == 0 or ielas == 1 or ielas == 2):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ielas)
        if ipreg is not None and not (isinstance(ipreg.value, types.Jump) or ipreg == 0 or ipreg == 1 or ipreg == 2 or ipreg == 3):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ipreg)
        if iexisa is not None and not (isinstance(iexisa.value, types.Jump) or iexisa == 0 or iexisa == 1 or iexisa == 2):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, iexisa)
        if jcoul is not None and not (isinstance(jcoul.value, types.Jump) or jcoul == 0 or jcoul == 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, jcoul)
        if nexite is not None and not (isinstance(nexite.value, types.Jump) or nexite == 0 or nexite == 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, nexite)
        if npidk is not None and not (isinstance(npidk.value, types.Jump) or npidk == 0 or npidk == 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, npidk)
        if noact is not None and not (isinstance(noact.value, types.Jump) or noact == -2 or noact == -1 or noact == 0 or noact == 1 or noact == 2):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, noact)
        if icem is not None and not (isinstance(icem.value, types.Jump) or icem == 0 or icem == 1 or icem == 2):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, icem)
        if ilaq is not None and not (isinstance(ilaq.value, types.Jump) or ilaq == 0 or ilaq == 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ilaq)

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


@dataclasses.dataclass
class LcaBuilder(_option.DataOptionBuilder):
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

    ielas: str | int | types.Integer = None
    ipreg: str | int | types.Integer = None
    iexisa: str | int | types.Integer = None
    ichoic: str | int | types.Integer = None
    jcoul: str | int | types.Integer = None
    nexite: str | int | types.Integer = None
    npidk: str | int | types.Integer = None
    noact: str | int | types.Integer = None
    icem: str | int | types.Integer = None
    ilaq: str | int | types.Integer = None
    nevtype: str | int | types.Integer = None

    def build(self):
        """
        Builds ``LcaBuilder`` into ``Lca``.

        Returns:
            ``Lca`` for ``LcaBuilder``.
        """

        ielas = self.ielas
        if isinstance(self.ielas, types.Integer):
            ielas = self.ielas
        elif isinstance(self.ielas, int):
            ielas = types.Integer(self.ielas)
        elif isinstance(self.ielas, str):
            ielas = types.Integer.from_mcnp(self.ielas)

        ipreg = self.ipreg
        if isinstance(self.ipreg, types.Integer):
            ipreg = self.ipreg
        elif isinstance(self.ipreg, int):
            ipreg = types.Integer(self.ipreg)
        elif isinstance(self.ipreg, str):
            ipreg = types.Integer.from_mcnp(self.ipreg)

        iexisa = self.iexisa
        if isinstance(self.iexisa, types.Integer):
            iexisa = self.iexisa
        elif isinstance(self.iexisa, int):
            iexisa = types.Integer(self.iexisa)
        elif isinstance(self.iexisa, str):
            iexisa = types.Integer.from_mcnp(self.iexisa)

        ichoic = self.ichoic
        if isinstance(self.ichoic, types.Integer):
            ichoic = self.ichoic
        elif isinstance(self.ichoic, int):
            ichoic = types.Integer(self.ichoic)
        elif isinstance(self.ichoic, str):
            ichoic = types.Integer.from_mcnp(self.ichoic)

        jcoul = self.jcoul
        if isinstance(self.jcoul, types.Integer):
            jcoul = self.jcoul
        elif isinstance(self.jcoul, int):
            jcoul = types.Integer(self.jcoul)
        elif isinstance(self.jcoul, str):
            jcoul = types.Integer.from_mcnp(self.jcoul)

        nexite = self.nexite
        if isinstance(self.nexite, types.Integer):
            nexite = self.nexite
        elif isinstance(self.nexite, int):
            nexite = types.Integer(self.nexite)
        elif isinstance(self.nexite, str):
            nexite = types.Integer.from_mcnp(self.nexite)

        npidk = self.npidk
        if isinstance(self.npidk, types.Integer):
            npidk = self.npidk
        elif isinstance(self.npidk, int):
            npidk = types.Integer(self.npidk)
        elif isinstance(self.npidk, str):
            npidk = types.Integer.from_mcnp(self.npidk)

        noact = self.noact
        if isinstance(self.noact, types.Integer):
            noact = self.noact
        elif isinstance(self.noact, int):
            noact = types.Integer(self.noact)
        elif isinstance(self.noact, str):
            noact = types.Integer.from_mcnp(self.noact)

        icem = self.icem
        if isinstance(self.icem, types.Integer):
            icem = self.icem
        elif isinstance(self.icem, int):
            icem = types.Integer(self.icem)
        elif isinstance(self.icem, str):
            icem = types.Integer.from_mcnp(self.icem)

        ilaq = self.ilaq
        if isinstance(self.ilaq, types.Integer):
            ilaq = self.ilaq
        elif isinstance(self.ilaq, int):
            ilaq = types.Integer(self.ilaq)
        elif isinstance(self.ilaq, str):
            ilaq = types.Integer.from_mcnp(self.ilaq)

        nevtype = self.nevtype
        if isinstance(self.nevtype, types.Integer):
            nevtype = self.nevtype
        elif isinstance(self.nevtype, int):
            nevtype = types.Integer(self.nevtype)
        elif isinstance(self.nevtype, str):
            nevtype = types.Integer.from_mcnp(self.nevtype)

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

    @staticmethod
    def unbuild(ast: Lca):
        """
        Unbuilds ``Lca`` into ``LcaBuilder``

        Returns:
            ``LcaBuilder`` for ``Lca``.
        """

        return LcaBuilder(
            ielas=copy.deepcopy(ast.ielas),
            ipreg=copy.deepcopy(ast.ipreg),
            iexisa=copy.deepcopy(ast.iexisa),
            ichoic=copy.deepcopy(ast.ichoic),
            jcoul=copy.deepcopy(ast.jcoul),
            nexite=copy.deepcopy(ast.nexite),
            npidk=copy.deepcopy(ast.npidk),
            noact=copy.deepcopy(ast.noact),
            icem=copy.deepcopy(ast.icem),
            ilaq=copy.deepcopy(ast.ilaq),
            nevtype=copy.deepcopy(ast.nevtype),
        )
