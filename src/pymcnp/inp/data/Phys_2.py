import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Phys_2(DataOption):
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
        rf'\Aphys:e( {types.RealOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?\Z'
    )

    def __init__(
        self,
        emax: types.RealOrJump = None,
        ides: types.IntegerOrJump = None,
        iphot: types.IntegerOrJump = None,
        ibad: types.IntegerOrJump = None,
        istrg: types.IntegerOrJump = None,
        bnum: types.RealOrJump = None,
        xnum: types.RealOrJump = None,
        rnok: types.IntegerOrJump = None,
        enum: types.IntegerOrJump = None,
        numb: types.IntegerOrJump = None,
        i_mcs_model: types.IntegerOrJump = None,
        efac: types.RealOrJump = None,
        electron_method_boundary: types.RealOrJump = None,
        ckvnum: types.RealOrJump = None,
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
            InpError: SEMANTICS_OPTION.
        """

        if ides is not None and not (isinstance(ides, types.Jump) or ides in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ides)
        if iphot is not None and not (isinstance(iphot, types.Jump) or iphot in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, iphot)
        if ibad is not None and not (isinstance(ibad, types.Jump) or ibad in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ibad)
        if istrg is not None and not (isinstance(istrg, types.Jump) or istrg in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, istrg)
        if xnum is not None and not (isinstance(xnum, types.Jump) or xnum >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, xnum)
        if rnok is not None and not (isinstance(rnok, types.Jump) or rnok >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, rnok)
        if enum is not None and not (isinstance(enum, types.Jump) or enum >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, enum)
        if numb is not None and not (isinstance(i_mcs_model, types.Jump) or i_mcs_model >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, numb)
        if i_mcs_model is not None and not (
            isinstance(i_mcs_model, types.Jump) or i_mcs_model in {-1, 0}
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, i_mcs_model)
        if efac is not None and not (isinstance(efac, types.Jump) or 0.8 <= efac <= 0.99):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, efac)
        if ckvnum is not None and not (isinstance(ckvnum, types.Jump) or 0 <= ckvnum < 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ckvnum)

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

    emax: str | float | types.RealOrJump = None
    ides: str | int | types.IntegerOrJump = None
    iphot: str | int | types.IntegerOrJump = None
    ibad: str | int | types.IntegerOrJump = None
    istrg: str | int | types.IntegerOrJump = None
    bnum: str | float | types.RealOrJump = None
    xnum: str | float | types.RealOrJump = None
    rnok: str | int | types.IntegerOrJump = None
    enum: str | int | types.IntegerOrJump = None
    numb: str | int | types.IntegerOrJump = None
    i_mcs_model: str | int | types.IntegerOrJump = None
    efac: str | float | types.RealOrJump = None
    electron_method_boundary: str | float | types.RealOrJump = None
    ckvnum: str | float | types.RealOrJump = None

    def build(self):
        """
        Builds ``PhysBuilder_2`` into ``Phys_2``.

        Returns:
            ``Phys_2`` for ``PhysBuilder_2``.
        """

        emax = None
        if isinstance(self.emax, types.Real):
            emax = self.emax
        elif isinstance(self.emax, float) or isinstance(self.emax, int):
            emax = types.RealOrJump(self.emax)
        elif isinstance(self.emax, str):
            emax = types.RealOrJump.from_mcnp(self.emax)

        ides = None
        if isinstance(self.ides, types.Integer):
            ides = self.ides
        elif isinstance(self.ides, int):
            ides = types.IntegerOrJump(self.ides)
        elif isinstance(self.ides, str):
            ides = types.IntegerOrJump.from_mcnp(self.ides)

        iphot = None
        if isinstance(self.iphot, types.Integer):
            iphot = self.iphot
        elif isinstance(self.iphot, int):
            iphot = types.IntegerOrJump(self.iphot)
        elif isinstance(self.iphot, str):
            iphot = types.IntegerOrJump.from_mcnp(self.iphot)

        ibad = None
        if isinstance(self.ibad, types.Integer):
            ibad = self.ibad
        elif isinstance(self.ibad, int):
            ibad = types.IntegerOrJump(self.ibad)
        elif isinstance(self.ibad, str):
            ibad = types.IntegerOrJump.from_mcnp(self.ibad)

        istrg = None
        if isinstance(self.istrg, types.Integer):
            istrg = self.istrg
        elif isinstance(self.istrg, int):
            istrg = types.IntegerOrJump(self.istrg)
        elif isinstance(self.istrg, str):
            istrg = types.IntegerOrJump.from_mcnp(self.istrg)

        bnum = None
        if isinstance(self.bnum, types.Real):
            bnum = self.bnum
        elif isinstance(self.bnum, float) or isinstance(self.bnum, int):
            bnum = types.RealOrJump(self.bnum)
        elif isinstance(self.bnum, str):
            bnum = types.RealOrJump.from_mcnp(self.bnum)

        xnum = None
        if isinstance(self.xnum, types.Real):
            xnum = self.xnum
        elif isinstance(self.xnum, float) or isinstance(self.xnum, int):
            xnum = types.RealOrJump(self.xnum)
        elif isinstance(self.xnum, str):
            xnum = types.RealOrJump.from_mcnp(self.xnum)

        rnok = None
        if isinstance(self.rnok, types.Integer):
            rnok = self.rnok
        elif isinstance(self.rnok, int):
            rnok = types.IntegerOrJump(self.rnok)
        elif isinstance(self.rnok, str):
            rnok = types.IntegerOrJump.from_mcnp(self.rnok)

        enum = None
        if isinstance(self.enum, types.Integer):
            enum = self.enum
        elif isinstance(self.enum, int):
            enum = types.IntegerOrJump(self.enum)
        elif isinstance(self.enum, str):
            enum = types.IntegerOrJump.from_mcnp(self.enum)

        numb = None
        if isinstance(self.numb, types.Integer):
            numb = self.numb
        elif isinstance(self.numb, int):
            numb = types.IntegerOrJump(self.numb)
        elif isinstance(self.numb, str):
            numb = types.IntegerOrJump.from_mcnp(self.numb)

        i_mcs_model = None
        if isinstance(self.i_mcs_model, types.Integer):
            i_mcs_model = self.i_mcs_model
        elif isinstance(self.i_mcs_model, int):
            i_mcs_model = types.IntegerOrJump(self.i_mcs_model)
        elif isinstance(self.i_mcs_model, str):
            i_mcs_model = types.IntegerOrJump.from_mcnp(self.i_mcs_model)

        efac = None
        if isinstance(self.efac, types.Real):
            efac = self.efac
        elif isinstance(self.efac, float) or isinstance(self.efac, int):
            efac = types.RealOrJump(self.efac)
        elif isinstance(self.efac, str):
            efac = types.RealOrJump.from_mcnp(self.efac)

        electron_method_boundary = None
        if isinstance(self.electron_method_boundary, types.Real):
            electron_method_boundary = self.electron_method_boundary
        elif isinstance(self.electron_method_boundary, float) or isinstance(
            self.electron_method_boundary, int
        ):
            electron_method_boundary = types.RealOrJump(self.electron_method_boundary)
        elif isinstance(self.electron_method_boundary, str):
            electron_method_boundary = types.RealOrJump.from_mcnp(self.electron_method_boundary)

        ckvnum = None
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
