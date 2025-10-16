import re

from . import _card
from .. import types
from .. import errors


class Phys_2(_card.Card):
    """
    Represents INP `phys` elements variation #2.
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
        'j': types.String,
        'efac': types.Real,
        'electron_method_boundary': types.Real,
        'ckvnum': types.Real,
    }

    _REGEX = re.compile(
        r'\Aphys:e(?: (\S+))?(?: (\S+))?(?: (\S+))?(?: (\S+))?(?: (\S+))?(?: (\S+))?(?: (\S+))?(?: (\S+))?(?: (\S+))?(?: (\S+))?(?: (\S+))?(?: (j j))?(?: (\S+))?(?: (\S+))?(?: (\S+))?\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        emax: str | int | float | types.Real = None,
        ides: str | int | types.Integer = None,
        iphot: str | int | types.Integer = None,
        ibad: str | int | types.Integer = None,
        istrg: str | int | types.Integer = None,
        bnum: str | int | float | types.Real = None,
        xnum: str | int | float | types.Real = None,
        rnok: str | int | types.Integer = None,
        enum: str | int | types.Integer = None,
        numb: str | int | types.Integer = None,
        i_mcs_model: str | int | types.Integer = None,
        j: str | types.String = None,
        efac: str | int | float | types.Real = None,
        electron_method_boundary: str | int | float | types.Real = None,
        ckvnum: str | int | float | types.Real = None,
    ):
        """
        Initializes `Phys_2`.

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
            j: Not used.
            efac: Stopping power energy spacing controls.
            electron_method_boundary: Single-event transport start sontrols.
            ckvnum: Crenkov photon emission scalar.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.emax: types.Real = emax
        self.ides: types.Integer = ides
        self.iphot: types.Integer = iphot
        self.ibad: types.Integer = ibad
        self.istrg: types.Integer = istrg
        self.bnum: types.Real = bnum
        self.xnum: types.Real = xnum
        self.rnok: types.Integer = rnok
        self.enum: types.Integer = enum
        self.numb: types.Integer = numb
        self.i_mcs_model: types.Integer = i_mcs_model
        self.j = j
        self.efac: types.Real = efac
        self.electron_method_boundary: types.Real = electron_method_boundary
        self.ckvnum: types.Real = ckvnum

    @property
    def emax(self) -> types.Real:
        """
        Upper limit for electron energy

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._emax

    @emax.setter
    def emax(self, emax: str | int | float | types.Real) -> None:
        """
        Sets `emax`.

        Parameters:
            emax: Upper limit for electron energy.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if emax is not None:
            if isinstance(emax, types.Real):
                emax = emax
            elif isinstance(emax, int) or isinstance(emax, float):
                emax = types.Real(emax)
            elif isinstance(emax, str):
                emax = types.Real.from_mcnp(emax)

        self._emax: types.Real = emax

    @property
    def ides(self) -> types.Integer:
        """
        Photon electron production controls

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ides

    @ides.setter
    def ides(self, ides: str | int | types.Integer) -> None:
        """
        Sets `ides`.

        Parameters:
            ides: Photon electron production controls.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ides is not None:
            if isinstance(ides, types.Integer):
                ides = ides
            elif isinstance(ides, int):
                ides = types.Integer(ides)
            elif isinstance(ides, str):
                ides = types.Integer.from_mcnp(ides)

        if ides is not None and not (isinstance(ides.value, types.Jump) or ides in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, ides)

        self._ides: types.Integer = ides

    @property
    def iphot(self) -> types.Integer:
        """
        Electron photon production controls

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._iphot

    @iphot.setter
    def iphot(self, iphot: str | int | types.Integer) -> None:
        """
        Sets `iphot`.

        Parameters:
            iphot: Electron photon production controls.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if iphot is not None:
            if isinstance(iphot, types.Integer):
                iphot = iphot
            elif isinstance(iphot, int):
                iphot = types.Integer(iphot)
            elif isinstance(iphot, str):
                iphot = types.Integer.from_mcnp(iphot)

        if iphot is not None and not (isinstance(iphot.value, types.Jump) or iphot in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, iphot)

        self._iphot: types.Integer = iphot

    @property
    def ibad(self) -> types.Integer:
        """
        Bremsstrahlung angular distribution method controls

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ibad

    @ibad.setter
    def ibad(self, ibad: str | int | types.Integer) -> None:
        """
        Sets `ibad`.

        Parameters:
            ibad: Bremsstrahlung angular distribution method controls.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ibad is not None:
            if isinstance(ibad, types.Integer):
                ibad = ibad
            elif isinstance(ibad, int):
                ibad = types.Integer(ibad)
            elif isinstance(ibad, str):
                ibad = types.Integer.from_mcnp(ibad)

        if ibad is not None and not (isinstance(ibad.value, types.Jump) or ibad in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, ibad)

        self._ibad: types.Integer = ibad

    @property
    def istrg(self) -> types.Integer:
        """
        Electron continuous-energy straggling controls

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._istrg

    @istrg.setter
    def istrg(self, istrg: str | int | types.Integer) -> None:
        """
        Sets `istrg`.

        Parameters:
            istrg: Electron continuous-energy straggling controls.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if istrg is not None:
            if isinstance(istrg, types.Integer):
                istrg = istrg
            elif isinstance(istrg, int):
                istrg = types.Integer(istrg)
            elif isinstance(istrg, str):
                istrg = types.Integer.from_mcnp(istrg)

        if istrg is not None and not (isinstance(istrg.value, types.Jump) or istrg in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, istrg)

        self._istrg: types.Integer = istrg

    @property
    def bnum(self) -> types.Real:
        """
        Bremsstrahlung photon production controls

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bnum

    @bnum.setter
    def bnum(self, bnum: str | int | float | types.Real) -> None:
        """
        Sets `bnum`.

        Parameters:
            bnum: Bremsstrahlung photon production controls.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bnum is not None:
            if isinstance(bnum, types.Real):
                bnum = bnum
            elif isinstance(bnum, int) or isinstance(bnum, float):
                bnum = types.Real(bnum)
            elif isinstance(bnum, str):
                bnum = types.Real.from_mcnp(bnum)

        self._bnum: types.Real = bnum

    @property
    def xnum(self) -> types.Real:
        """
        Sampling of electron-induced x-rays controls

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._xnum

    @xnum.setter
    def xnum(self, xnum: str | int | float | types.Real) -> None:
        """
        Sets `xnum`.

        Parameters:
            xnum: Sampling of electron-induced x-rays controls.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if xnum is not None:
            if isinstance(xnum, types.Real):
                xnum = xnum
            elif isinstance(xnum, int) or isinstance(xnum, float):
                xnum = types.Real(xnum)
            elif isinstance(xnum, str):
                xnum = types.Real.from_mcnp(xnum)

        if xnum is not None and not (isinstance(xnum.value, types.Jump) or xnum >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, xnum)

        self._xnum: types.Real = xnum

    @property
    def rnok(self) -> types.Integer:
        """
        Knock-on electron creation controls

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._rnok

    @rnok.setter
    def rnok(self, rnok: str | int | types.Integer) -> None:
        """
        Sets `rnok`.

        Parameters:
            rnok: Knock-on electron creation controls.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if rnok is not None:
            if isinstance(rnok, types.Integer):
                rnok = rnok
            elif isinstance(rnok, int):
                rnok = types.Integer(rnok)
            elif isinstance(rnok, str):
                rnok = types.Integer.from_mcnp(rnok)

        if rnok is not None and not (isinstance(rnok.value, types.Jump) or rnok >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, rnok)

        self._rnok: types.Integer = rnok

    @property
    def enum(self) -> types.Integer:
        """
        Photon-induced secondary electron creation controls

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._enum

    @enum.setter
    def enum(self, enum: str | int | types.Integer) -> None:
        """
        Sets `enum`.

        Parameters:
            enum: Photon-induced secondary electron creation controls.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if enum is not None:
            if isinstance(enum, types.Integer):
                enum = enum
            elif isinstance(enum, int):
                enum = types.Integer(enum)
            elif isinstance(enum, str):
                enum = types.Integer.from_mcnp(enum)

        if enum is not None and not (isinstance(enum.value, types.Jump) or enum >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, enum)

        self._enum: types.Integer = enum

    @property
    def numb(self) -> types.Integer:
        """
        Bremsstrahlung electron creation controls

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._numb

    @numb.setter
    def numb(self, numb: str | int | types.Integer) -> None:
        """
        Sets `numb`.

        Parameters:
            numb: Bremsstrahlung electron creation controls.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if numb is not None:
            if isinstance(numb, types.Integer):
                numb = numb
            elif isinstance(numb, int):
                numb = types.Integer(numb)
            elif isinstance(numb, str):
                numb = types.Integer.from_mcnp(numb)

        if numb is not None and not (isinstance(numb.value, types.Jump) or numb >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, numb)

        self._numb: types.Integer = numb

    @property
    def i_mcs_model(self) -> types.Integer:
        """
        Choice of Coulomb scattering model controls

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._i_mcs_model

    @i_mcs_model.setter
    def i_mcs_model(self, i_mcs_model: str | int | types.Integer) -> None:
        """
        Sets `i_mcs_model`.

        Parameters:
            i_mcs_model: Choice of Coulomb scattering model controls.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if i_mcs_model is not None:
            if isinstance(i_mcs_model, types.Integer):
                i_mcs_model = i_mcs_model
            elif isinstance(i_mcs_model, int):
                i_mcs_model = types.Integer(i_mcs_model)
            elif isinstance(i_mcs_model, str):
                i_mcs_model = types.Integer.from_mcnp(i_mcs_model)

        if i_mcs_model is not None and not (isinstance(i_mcs_model.value, types.Jump) or i_mcs_model in {-1, 0}):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, i_mcs_model)

        self._i_mcs_model: types.Integer = i_mcs_model

    @property
    def j(self) -> types.Real:
        """
        Not used.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._j

    @j.setter
    def j(self, j: str | types.String) -> None:
        """
        Sets `j`.

        Parameters:
            j: Not used.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if j is not None:
            if isinstance(j, types.String):
                j = j
            elif isinstance(j, str):
                j = types.String.from_mcnp(j)

        if j is not None and j.value.lower() not in {'j j'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, j)

        self._j: types.String = j

    @property
    def efac(self) -> types.Real:
        """
        Stopping power energy spacing controls

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._efac

    @efac.setter
    def efac(self, efac: str | int | float | types.Real) -> None:
        """
        Sets `efac`.

        Parameters:
            efac: Stopping power energy spacing controls.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if efac is not None:
            if isinstance(efac, types.Real):
                efac = efac
            elif isinstance(efac, int) or isinstance(efac, float):
                efac = types.Real(efac)
            elif isinstance(efac, str):
                efac = types.Real.from_mcnp(efac)

        if efac is not None and not (isinstance(efac.value, types.Jump) or (efac >= 0.8 and efac <= 0.99)):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, efac)

        self._efac: types.Real = efac

    @property
    def electron_method_boundary(self) -> types.Real:
        """
        Single-event transport start sontrols

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._electron_method_boundary

    @electron_method_boundary.setter
    def electron_method_boundary(self, electron_method_boundary: str | int | float | types.Real) -> None:
        """
        Sets `electron_method_boundary`.

        Parameters:
            electron_method_boundary: Single-event transport start sontrols.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if electron_method_boundary is not None:
            if isinstance(electron_method_boundary, types.Real):
                electron_method_boundary = electron_method_boundary
            elif isinstance(electron_method_boundary, int) or isinstance(electron_method_boundary, float):
                electron_method_boundary = types.Real(electron_method_boundary)
            elif isinstance(electron_method_boundary, str):
                electron_method_boundary = types.Real.from_mcnp(electron_method_boundary)

        self._electron_method_boundary: types.Real = electron_method_boundary

    @property
    def ckvnum(self) -> types.Real:
        """
        Crenkov photon emission scalar

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ckvnum

    @ckvnum.setter
    def ckvnum(self, ckvnum: str | int | float | types.Real) -> None:
        """
        Sets `ckvnum`.

        Parameters:
            ckvnum: Crenkov photon emission scalar.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ckvnum is not None:
            if isinstance(ckvnum, types.Real):
                ckvnum = ckvnum
            elif isinstance(ckvnum, int) or isinstance(ckvnum, float):
                ckvnum = types.Real(ckvnum)
            elif isinstance(ckvnum, str):
                ckvnum = types.Real.from_mcnp(ckvnum)

        if ckvnum is not None and not (isinstance(ckvnum.value, types.Jump) or ckvnum >= 0 and ckvnum < 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, ckvnum)

        self._ckvnum: types.Real = ckvnum
