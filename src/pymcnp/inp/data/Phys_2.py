import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Phys_2(_option.DataOption):
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

    _KEYWORD = 'phys:e'

    _ATTRS = {
        'emax': types.Real,
        'ides': types.Integer,
        'iphot': types.Integer,
        'ibad': types.Integer,
        'istrg': types.Integer,
        'bnum': types.Real,
        'xnum': types.Real,
        'rnok': types.Integer,
        'enum': types.Integer,
        'numb': types.Integer,
        'i_mcs_model': types.Integer,
        'efac': types.Real,
        'electron_method_boundary': types.Real,
        'ckvnum': types.Real,
    }

    _REGEX = re.compile(
        r'\Aphys:e(?: (\S+))?(?: (\S+))?(?: (\S+))?(?: (\S+))?(?: (\S+))?(?: (\S+))?(?: (\S+))?(?: (\S+))?(?: (\S+))?(?: (\S+))?(?: (\S+))?(?: (\S+))?(?: (\S+))?(?: (\S+))?(?: (\S+))?\Z'
    )

    def __init__(
        self,
        emax: types.Real = None,
        ides: types.Integer = None,
        iphot: types.Integer = None,
        ibad: types.Integer = None,
        istrg: types.Integer = None,
        bnum: types.Real = None,
        xnum: types.Real = None,
        rnok: types.Integer = None,
        enum: types.Integer = None,
        numb: types.Integer = None,
        i_mcs_model: types.Integer = None,
        efac: types.Real = None,
        electron_method_boundary: types.Real = None,
        ckvnum: types.Real = None,
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

        if ides is not None and not (isinstance(ides.value, types.Jump) or ides in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ides)
        if iphot is not None and not (isinstance(iphot.value, types.Jump) or iphot in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, iphot)
        if ibad is not None and not (isinstance(ibad.value, types.Jump) or ibad in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ibad)
        if istrg is not None and not (isinstance(istrg.value, types.Jump) or istrg in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, istrg)
        if xnum is not None and not (isinstance(xnum.value, types.Jump) or xnum >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, xnum)
        if rnok is not None and not (isinstance(rnok.value, types.Jump) or rnok >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, rnok)
        if enum is not None and not (isinstance(enum.value, types.Jump) or enum >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, enum)
        if numb is not None and not (isinstance(numb.value, types.Jump) or numb >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, numb)
        if i_mcs_model is not None and not (isinstance(i_mcs_model.value, types.Jump) or i_mcs_model in {-1, 0}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, i_mcs_model)
        if efac is not None and not (isinstance(efac.value, types.Jump) or (efac >= 0.8 and efac <= 0.99)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, efac)
        if ckvnum is not None and not (isinstance(ckvnum.value, types.Jump) or ckvnum >= 0 and ckvnum < 1):
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

        self.emax: typing.Final[types.Real] = emax
        self.ides: typing.Final[types.Integer] = ides
        self.iphot: typing.Final[types.Integer] = iphot
        self.ibad: typing.Final[types.Integer] = ibad
        self.istrg: typing.Final[types.Integer] = istrg
        self.bnum: typing.Final[types.Real] = bnum
        self.xnum: typing.Final[types.Real] = xnum
        self.rnok: typing.Final[types.Integer] = rnok
        self.enum: typing.Final[types.Integer] = enum
        self.numb: typing.Final[types.Integer] = numb
        self.i_mcs_model: typing.Final[types.Integer] = i_mcs_model
        self.efac: typing.Final[types.Real] = efac
        self.electron_method_boundary: typing.Final[types.Real] = electron_method_boundary
        self.ckvnum: typing.Final[types.Real] = ckvnum


@dataclasses.dataclass
class PhysBuilder_2(_option.DataOptionBuilder):
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

    emax: str | float | types.Real = None
    ides: str | int | types.Integer = None
    iphot: str | int | types.Integer = None
    ibad: str | int | types.Integer = None
    istrg: str | int | types.Integer = None
    bnum: str | float | types.Real = None
    xnum: str | float | types.Real = None
    rnok: str | int | types.Integer = None
    enum: str | int | types.Integer = None
    numb: str | int | types.Integer = None
    i_mcs_model: str | int | types.Integer = None
    efac: str | float | types.Real = None
    electron_method_boundary: str | float | types.Real = None
    ckvnum: str | float | types.Real = None

    def build(self):
        """
        Builds ``PhysBuilder_2`` into ``Phys_2``.

        Returns:
            ``Phys_2`` for ``PhysBuilder_2``.
        """

        emax = self.emax
        if isinstance(self.emax, types.Real):
            emax = self.emax
        elif isinstance(self.emax, float) or isinstance(self.emax, int):
            emax = types.Real(self.emax)
        elif isinstance(self.emax, str):
            emax = types.Real.from_mcnp(self.emax)

        ides = self.ides
        if isinstance(self.ides, types.Integer):
            ides = self.ides
        elif isinstance(self.ides, int):
            ides = types.Integer(self.ides)
        elif isinstance(self.ides, str):
            ides = types.Integer.from_mcnp(self.ides)

        iphot = self.iphot
        if isinstance(self.iphot, types.Integer):
            iphot = self.iphot
        elif isinstance(self.iphot, int):
            iphot = types.Integer(self.iphot)
        elif isinstance(self.iphot, str):
            iphot = types.Integer.from_mcnp(self.iphot)

        ibad = self.ibad
        if isinstance(self.ibad, types.Integer):
            ibad = self.ibad
        elif isinstance(self.ibad, int):
            ibad = types.Integer(self.ibad)
        elif isinstance(self.ibad, str):
            ibad = types.Integer.from_mcnp(self.ibad)

        istrg = self.istrg
        if isinstance(self.istrg, types.Integer):
            istrg = self.istrg
        elif isinstance(self.istrg, int):
            istrg = types.Integer(self.istrg)
        elif isinstance(self.istrg, str):
            istrg = types.Integer.from_mcnp(self.istrg)

        bnum = self.bnum
        if isinstance(self.bnum, types.Real):
            bnum = self.bnum
        elif isinstance(self.bnum, float) or isinstance(self.bnum, int):
            bnum = types.Real(self.bnum)
        elif isinstance(self.bnum, str):
            bnum = types.Real.from_mcnp(self.bnum)

        xnum = self.xnum
        if isinstance(self.xnum, types.Real):
            xnum = self.xnum
        elif isinstance(self.xnum, float) or isinstance(self.xnum, int):
            xnum = types.Real(self.xnum)
        elif isinstance(self.xnum, str):
            xnum = types.Real.from_mcnp(self.xnum)

        rnok = self.rnok
        if isinstance(self.rnok, types.Integer):
            rnok = self.rnok
        elif isinstance(self.rnok, int):
            rnok = types.Integer(self.rnok)
        elif isinstance(self.rnok, str):
            rnok = types.Integer.from_mcnp(self.rnok)

        enum = self.enum
        if isinstance(self.enum, types.Integer):
            enum = self.enum
        elif isinstance(self.enum, int):
            enum = types.Integer(self.enum)
        elif isinstance(self.enum, str):
            enum = types.Integer.from_mcnp(self.enum)

        numb = self.numb
        if isinstance(self.numb, types.Integer):
            numb = self.numb
        elif isinstance(self.numb, int):
            numb = types.Integer(self.numb)
        elif isinstance(self.numb, str):
            numb = types.Integer.from_mcnp(self.numb)

        i_mcs_model = self.i_mcs_model
        if isinstance(self.i_mcs_model, types.Integer):
            i_mcs_model = self.i_mcs_model
        elif isinstance(self.i_mcs_model, int):
            i_mcs_model = types.Integer(self.i_mcs_model)
        elif isinstance(self.i_mcs_model, str):
            i_mcs_model = types.Integer.from_mcnp(self.i_mcs_model)

        efac = self.efac
        if isinstance(self.efac, types.Real):
            efac = self.efac
        elif isinstance(self.efac, float) or isinstance(self.efac, int):
            efac = types.Real(self.efac)
        elif isinstance(self.efac, str):
            efac = types.Real.from_mcnp(self.efac)

        electron_method_boundary = self.electron_method_boundary
        if isinstance(self.electron_method_boundary, types.Real):
            electron_method_boundary = self.electron_method_boundary
        elif isinstance(self.electron_method_boundary, float) or isinstance(self.electron_method_boundary, int):
            electron_method_boundary = types.Real(self.electron_method_boundary)
        elif isinstance(self.electron_method_boundary, str):
            electron_method_boundary = types.Real.from_mcnp(self.electron_method_boundary)

        ckvnum = self.ckvnum
        if isinstance(self.ckvnum, types.Real):
            ckvnum = self.ckvnum
        elif isinstance(self.ckvnum, float) or isinstance(self.ckvnum, int):
            ckvnum = types.Real(self.ckvnum)
        elif isinstance(self.ckvnum, str):
            ckvnum = types.Real.from_mcnp(self.ckvnum)

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

    @staticmethod
    def unbuild(ast: Phys_2):
        """
        Unbuilds ``Phys_2`` into ``PhysBuilder_2``

        Returns:
            ``PhysBuilder_2`` for ``Phys_2``.
        """

        return PhysBuilder_2(
            emax=copy.deepcopy(ast.emax),
            ides=copy.deepcopy(ast.ides),
            iphot=copy.deepcopy(ast.iphot),
            ibad=copy.deepcopy(ast.ibad),
            istrg=copy.deepcopy(ast.istrg),
            bnum=copy.deepcopy(ast.bnum),
            xnum=copy.deepcopy(ast.xnum),
            rnok=copy.deepcopy(ast.rnok),
            enum=copy.deepcopy(ast.enum),
            numb=copy.deepcopy(ast.numb),
            i_mcs_model=copy.deepcopy(ast.i_mcs_model),
            efac=copy.deepcopy(ast.efac),
            electron_method_boundary=copy.deepcopy(ast.electron_method_boundary),
            ckvnum=copy.deepcopy(ast.ckvnum),
        )
