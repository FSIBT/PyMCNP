import re
import typing
import dataclasses


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Phys_2(DataOption_, keyword='phys:e'):
    """
    Represents INP phys variation #2 elements.

    Attributes:
        emax: Upper limit for electron energy.
        ides: Photon electron production controls.
        iphot: Electron photon production controls.
        ibad: Bremsstrahlung angular distribution method controls.
        istrg: Electron continuous-energy straggling controls.
        bnum: Bremsstrahlung photon production controls.
        xnum: Sampling of electron-induced x-rays controls.
        rnok: Knock-on electron creation controls.
        enum: Photon-induced secondary electron creation controls.
        numb: Bremsstrahlung electron creation controls.
        i_mcs_model: Choice of Coulomb scattering model controls.
        efac: Stopping power energy spacing controls.
        electron_method_boundary: Single-event transport start sontrols.
        ckvnum: Crenkov photon emission scalar.
    """

    _ATTRS = {
        'emax': types.RealOrJump,
        'ides': types.IntegerOrJump,
        'iphot': types.IntegerOrJump,
        'ibad': types.IntegerOrJump,
        'istrg': types.IntegerOrJump,
        'bnum': types.RealOrJump,
        'xnum': types.RealOrJump,
        'rnok': types.IntegerOrJump,
        'enum': types.IntegerOrJump,
        'numb': types.IntegerOrJump,
        'i_mcs_model': types.IntegerOrJump,
        'efac': types.RealOrJump,
        'electron_method_boundary': types.RealOrJump,
        'ckvnum': types.RealOrJump,
    }

    _REGEX = re.compile(
        rf'\Aphys:e( {types.RealOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        emax: types.RealOrJump,
        ides: types.IntegerOrJump,
        iphot: types.IntegerOrJump,
        ibad: types.IntegerOrJump,
        istrg: types.IntegerOrJump,
        bnum: types.RealOrJump,
        xnum: types.RealOrJump,
        rnok: types.IntegerOrJump,
        enum: types.IntegerOrJump,
        numb: types.IntegerOrJump,
        i_mcs_model: types.IntegerOrJump,
        efac: types.RealOrJump,
        electron_method_boundary: types.RealOrJump,
        ckvnum: types.RealOrJump,
    ):
        """
        Initializes ``Phys_2``.

        Parameters:
            emax: Upper limit for electron energy.
            ides: Photon electron production controls.
            iphot: Electron photon production controls.
            ibad: Bremsstrahlung angular distribution method controls.
            istrg: Electron continuous-energy straggling controls.
            bnum: Bremsstrahlung photon production controls.
            xnum: Sampling of electron-induced x-rays controls.
            rnok: Knock-on electron creation controls.
            enum: Photon-induced secondary electron creation controls.
            numb: Bremsstrahlung electron creation controls.
            i_mcs_model: Choice of Coulomb scattering model controls.
            efac: Stopping power energy spacing controls.
            electron_method_boundary: Single-event transport start sontrols.
            ckvnum: Crenkov photon emission scalar.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if emax is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, emax)
        if ides is None or ides not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ides)
        if iphot is None or iphot not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, iphot)
        if ibad is None or ibad not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ibad)
        if istrg is None or istrg not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, istrg)
        if bnum is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bnum)
        if xnum is None or not (xnum >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, xnum)
        if rnok is None or not (rnok >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, rnok)
        if enum is None or not (enum >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, enum)
        if numb is None or not (i_mcs_model >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, numb)
        if i_mcs_model is None or i_mcs_model not in {-1, 0}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, i_mcs_model)
        if efac is None or not (0.8 <= efac <= 0.99):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, efac)
        if electron_method_boundary is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, electron_method_boundary)
        if ckvnum is None or not (0 <= ckvnum < 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ckvnum)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                emax,
                ides,
                iphot,
                ibad,
                istrg,
                bnum,
                xnum,
                rnok,
                enum,
                numb,
                i_mcs_model,
                efac,
                electron_method_boundary,
                ckvnum,
            ]
        )

        self.emax: typing.Final[types.RealOrJump] = emax
        self.ides: typing.Final[types.IntegerOrJump] = ides
        self.iphot: typing.Final[types.IntegerOrJump] = iphot
        self.ibad: typing.Final[types.IntegerOrJump] = ibad
        self.istrg: typing.Final[types.IntegerOrJump] = istrg
        self.bnum: typing.Final[types.RealOrJump] = bnum
        self.xnum: typing.Final[types.RealOrJump] = xnum
        self.rnok: typing.Final[types.IntegerOrJump] = rnok
        self.enum: typing.Final[types.IntegerOrJump] = enum
        self.numb: typing.Final[types.IntegerOrJump] = numb
        self.i_mcs_model: typing.Final[types.IntegerOrJump] = i_mcs_model
        self.efac: typing.Final[types.RealOrJump] = efac
        self.electron_method_boundary: typing.Final[types.RealOrJump] = electron_method_boundary
        self.ckvnum: typing.Final[types.RealOrJump] = ckvnum


@dataclasses.dataclass
class PhysBuilder_2:
    """
    Builds ``Phys_2``.

    Attributes:
        emax: Upper limit for electron energy.
        ides: Photon electron production controls.
        iphot: Electron photon production controls.
        ibad: Bremsstrahlung angular distribution method controls.
        istrg: Electron continuous-energy straggling controls.
        bnum: Bremsstrahlung photon production controls.
        xnum: Sampling of electron-induced x-rays controls.
        rnok: Knock-on electron creation controls.
        enum: Photon-induced secondary electron creation controls.
        numb: Bremsstrahlung electron creation controls.
        i_mcs_model: Choice of Coulomb scattering model controls.
        efac: Stopping power energy spacing controls.
        electron_method_boundary: Single-event transport start sontrols.
        ckvnum: Crenkov photon emission scalar.
    """

    emax: str | float | types.RealOrJump
    ides: str | int | types.IntegerOrJump
    iphot: str | int | types.IntegerOrJump
    ibad: str | int | types.IntegerOrJump
    istrg: str | int | types.IntegerOrJump
    bnum: str | float | types.RealOrJump
    xnum: str | float | types.RealOrJump
    rnok: str | int | types.IntegerOrJump
    enum: str | int | types.IntegerOrJump
    numb: str | int | types.IntegerOrJump
    i_mcs_model: str | int | types.IntegerOrJump
    efac: str | float | types.RealOrJump
    electron_method_boundary: str | float | types.RealOrJump
    ckvnum: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``PhysBuilder_2`` into ``Phys_2``.

        Returns:
            ``Phys_2`` for ``PhysBuilder_2``.
        """

        if isinstance(self.emax, types.Real):
            emax = self.emax
        elif isinstance(self.emax, float) or isinstance(self.emax, int):
            emax = types.RealOrJump(self.emax)
        elif isinstance(self.emax, str):
            emax = types.RealOrJump.from_mcnp(self.emax)

        if isinstance(self.ides, types.Integer):
            ides = self.ides
        elif isinstance(self.ides, int):
            ides = types.IntegerOrJump(self.ides)
        elif isinstance(self.ides, str):
            ides = types.IntegerOrJump.from_mcnp(self.ides)

        if isinstance(self.iphot, types.Integer):
            iphot = self.iphot
        elif isinstance(self.iphot, int):
            iphot = types.IntegerOrJump(self.iphot)
        elif isinstance(self.iphot, str):
            iphot = types.IntegerOrJump.from_mcnp(self.iphot)

        if isinstance(self.ibad, types.Integer):
            ibad = self.ibad
        elif isinstance(self.ibad, int):
            ibad = types.IntegerOrJump(self.ibad)
        elif isinstance(self.ibad, str):
            ibad = types.IntegerOrJump.from_mcnp(self.ibad)

        if isinstance(self.istrg, types.Integer):
            istrg = self.istrg
        elif isinstance(self.istrg, int):
            istrg = types.IntegerOrJump(self.istrg)
        elif isinstance(self.istrg, str):
            istrg = types.IntegerOrJump.from_mcnp(self.istrg)

        if isinstance(self.bnum, types.Real):
            bnum = self.bnum
        elif isinstance(self.bnum, float) or isinstance(self.bnum, int):
            bnum = types.RealOrJump(self.bnum)
        elif isinstance(self.bnum, str):
            bnum = types.RealOrJump.from_mcnp(self.bnum)

        if isinstance(self.xnum, types.Real):
            xnum = self.xnum
        elif isinstance(self.xnum, float) or isinstance(self.xnum, int):
            xnum = types.RealOrJump(self.xnum)
        elif isinstance(self.xnum, str):
            xnum = types.RealOrJump.from_mcnp(self.xnum)

        if isinstance(self.rnok, types.Integer):
            rnok = self.rnok
        elif isinstance(self.rnok, int):
            rnok = types.IntegerOrJump(self.rnok)
        elif isinstance(self.rnok, str):
            rnok = types.IntegerOrJump.from_mcnp(self.rnok)

        if isinstance(self.enum, types.Integer):
            enum = self.enum
        elif isinstance(self.enum, int):
            enum = types.IntegerOrJump(self.enum)
        elif isinstance(self.enum, str):
            enum = types.IntegerOrJump.from_mcnp(self.enum)

        if isinstance(self.numb, types.Integer):
            numb = self.numb
        elif isinstance(self.numb, int):
            numb = types.IntegerOrJump(self.numb)
        elif isinstance(self.numb, str):
            numb = types.IntegerOrJump.from_mcnp(self.numb)

        if isinstance(self.i_mcs_model, types.Integer):
            i_mcs_model = self.i_mcs_model
        elif isinstance(self.i_mcs_model, int):
            i_mcs_model = types.IntegerOrJump(self.i_mcs_model)
        elif isinstance(self.i_mcs_model, str):
            i_mcs_model = types.IntegerOrJump.from_mcnp(self.i_mcs_model)

        if isinstance(self.efac, types.Real):
            efac = self.efac
        elif isinstance(self.efac, float) or isinstance(self.efac, int):
            efac = types.RealOrJump(self.efac)
        elif isinstance(self.efac, str):
            efac = types.RealOrJump.from_mcnp(self.efac)

        if isinstance(self.electron_method_boundary, types.Real):
            electron_method_boundary = self.electron_method_boundary
        elif isinstance(self.electron_method_boundary, float) or isinstance(
            self.electron_method_boundary, int
        ):
            electron_method_boundary = types.RealOrJump(self.electron_method_boundary)
        elif isinstance(self.electron_method_boundary, str):
            electron_method_boundary = types.RealOrJump.from_mcnp(self.electron_method_boundary)

        if isinstance(self.ckvnum, types.Real):
            ckvnum = self.ckvnum
        elif isinstance(self.ckvnum, float) or isinstance(self.ckvnum, int):
            ckvnum = types.RealOrJump(self.ckvnum)
        elif isinstance(self.ckvnum, str):
            ckvnum = types.RealOrJump.from_mcnp(self.ckvnum)

        return Phys_2(
            emax=emax,
            ides=ides,
            iphot=iphot,
            ibad=ibad,
            istrg=istrg,
            bnum=bnum,
            xnum=xnum,
            rnok=rnok,
            enum=enum,
            numb=numb,
            i_mcs_model=i_mcs_model,
            efac=efac,
            electron_method_boundary=electron_method_boundary,
            ckvnum=ckvnum,
        )
