import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Lca(DataOption_, keyword='lca'):
    """
    Represents INP lca elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
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
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if ielas is None or not (ielas == 0 or ielas == 1 or ielas == 2):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ielas)
        if ipreg is None or not (ipreg == 0 or ipreg == 1 or ipreg == 2 or ipreg == 3):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ipreg)
        if iexisa is None or not (iexisa == 0 or iexisa == 1 or iexisa == 2):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, iexisa)
        if ichoic is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ichoic)
        if jcoul is None or not (jcoul == 0 or jcoul == 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, jcoul)
        if nexite is None or not (nexite == 0 or nexite == 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, nexite)
        if npidk is None or not (npidk == 0 or npidk == 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, npidk)
        if noact is None or not (
            noact == -2 or noact == -1 or noact == 0 or noact == 1 or noact == 2
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, noact)
        if icem is None or not (icem == 0 or icem == 1 or icem == 2):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, icem)
        if ilaq is None or not (ilaq == 0 or ilaq == 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ilaq)
        if nevtype is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, nevtype)

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
