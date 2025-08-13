import re

from . import _card
from .. import types
from .. import errors


class Phys_3(_card.Card):
    """
    Represents INP `phys` elements variation #3.
    """

    _KEYWORD = 'phys:h'

    _ATTRS = {
        'emax': types.Real,
        'ean': types.Real,
        'tabl': types.Real,
        'istrg': types.Integer,
        'recl': types.Real,
        'i_mcs_model': types.Integer,
        'i_int_model': types.Integer,
        'i_els_model': types.Integer,
        'efac': types.Real,
        'ckvnum': types.Real,
        'drp': types.Real,
    }

    _REGEX = re.compile(
        rf'\Aphys:h( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        emax: str | int | float | types.Real = None,
        ean: str | int | float | types.Real = None,
        tabl: str | int | float | types.Real = None,
        istrg: str | int | types.Integer = None,
        recl: str | int | float | types.Real = None,
        i_mcs_model: str | int | types.Integer = None,
        i_int_model: str | int | types.Integer = None,
        i_els_model: str | int | types.Integer = None,
        efac: str | int | float | types.Real = None,
        ckvnum: str | int | float | types.Real = None,
        drp: str | int | float | types.Real = None,
    ):
        """
        Initializes `Phys_3`.

        Parameters:
            emax: Upper proton energy limit.
            ean: Analog energy limit.
            tabl: Table-based physics cutoff.
            istrg: Charged-particle straggling controls.
            recl: Light ion recoil control.
            i_mcs_model: Choice of Coulomb scattering model controls.
            i_int_model: Treatment of nuclear interactions controls.
            i_els_model: Treatment of nuclear elastic scattering controls.
            efac: Stopping power energy spacing.
            ckvnum: Crenkov photon emission scalar.
            drp: Lower energy delta-ray cutoff.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.emax: types.Real = emax
        self.ean: types.Real = ean
        self.tabl: types.Real = tabl
        self.istrg: types.Integer = istrg
        self.recl: types.Real = recl
        self.i_mcs_model: types.Integer = i_mcs_model
        self.i_int_model: types.Integer = i_int_model
        self.i_els_model: types.Integer = i_els_model
        self.efac: types.Real = efac
        self.ckvnum: types.Real = ckvnum
        self.drp: types.Real = drp

    @property
    def emax(self) -> types.Real:
        """
        Upper proton energy limit

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
            emax: Upper proton energy limit.

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
    def ean(self) -> types.Real:
        """
        Analog energy limit

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ean

    @ean.setter
    def ean(self, ean: str | int | float | types.Real) -> None:
        """
        Sets `ean`.

        Parameters:
            ean: Analog energy limit.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ean is not None:
            if isinstance(ean, types.Real):
                ean = ean
            elif isinstance(ean, int) or isinstance(ean, float):
                ean = types.Real(ean)
            elif isinstance(ean, str):
                ean = types.Real.from_mcnp(ean)

        self._ean: types.Real = ean

    @property
    def tabl(self) -> types.Real:
        """
        Table-based physics cutoff

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._tabl

    @tabl.setter
    def tabl(self, tabl: str | int | float | types.Real) -> None:
        """
        Sets `tabl`.

        Parameters:
            tabl: Table-based physics cutoff.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if tabl is not None:
            if isinstance(tabl, types.Real):
                tabl = tabl
            elif isinstance(tabl, int) or isinstance(tabl, float):
                tabl = types.Real(tabl)
            elif isinstance(tabl, str):
                tabl = types.Real.from_mcnp(tabl)

        if tabl is not None and not (isinstance(tabl.value, types.Jump) or tabl == -1 or tabl >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, tabl)

        self._tabl: types.Real = tabl

    @property
    def istrg(self) -> types.Integer:
        """
        Charged-particle straggling controls

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
            istrg: Charged-particle straggling controls.

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
    def recl(self) -> types.Real:
        """
        Light ion recoil control

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._recl

    @recl.setter
    def recl(self, recl: str | int | float | types.Real) -> None:
        """
        Sets `recl`.

        Parameters:
            recl: Light ion recoil control.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if recl is not None:
            if isinstance(recl, types.Real):
                recl = recl
            elif isinstance(recl, int) or isinstance(recl, float):
                recl = types.Real(recl)
            elif isinstance(recl, str):
                recl = types.Real.from_mcnp(recl)

        if recl is not None and not (isinstance(recl.value, types.Jump) or (recl >= 0 and recl <= 1)):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, recl)

        self._recl: types.Real = recl

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

        if i_mcs_model is not None and not (isinstance(i_mcs_model.value, types.Jump) or i_mcs_model in {-1, 0, 1, 2}):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, i_mcs_model)

        self._i_mcs_model: types.Integer = i_mcs_model

    @property
    def i_int_model(self) -> types.Integer:
        """
        Treatment of nuclear interactions controls

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._i_int_model

    @i_int_model.setter
    def i_int_model(self, i_int_model: str | int | types.Integer) -> None:
        """
        Sets `i_int_model`.

        Parameters:
            i_int_model: Treatment of nuclear interactions controls.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if i_int_model is not None:
            if isinstance(i_int_model, types.Integer):
                i_int_model = i_int_model
            elif isinstance(i_int_model, int):
                i_int_model = types.Integer(i_int_model)
            elif isinstance(i_int_model, str):
                i_int_model = types.Integer.from_mcnp(i_int_model)

        if i_int_model is not None and not (isinstance(i_int_model.value, types.Jump) or i_int_model in {-1, 0, 1, 2}):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, i_int_model)

        self._i_int_model: types.Integer = i_int_model

    @property
    def i_els_model(self) -> types.Integer:
        """
        Treatment of nuclear elastic scattering controls

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._i_els_model

    @i_els_model.setter
    def i_els_model(self, i_els_model: str | int | types.Integer) -> None:
        """
        Sets `i_els_model`.

        Parameters:
            i_els_model: Treatment of nuclear elastic scattering controls.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if i_els_model is not None:
            if isinstance(i_els_model, types.Integer):
                i_els_model = i_els_model
            elif isinstance(i_els_model, int):
                i_els_model = types.Integer(i_els_model)
            elif isinstance(i_els_model, str):
                i_els_model = types.Integer.from_mcnp(i_els_model)

        if i_els_model is not None and not (isinstance(i_els_model.value, types.Jump) or i_els_model in {-1, 0}):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, i_els_model)

        self._i_els_model: types.Integer = i_els_model

    @property
    def efac(self) -> types.Real:
        """
        Stopping power energy spacing

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
            efac: Stopping power energy spacing.

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

    @property
    def drp(self) -> types.Real:
        """
        Lower energy delta-ray cutoff

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._drp

    @drp.setter
    def drp(self, drp: str | int | float | types.Real) -> None:
        """
        Sets `drp`.

        Parameters:
            drp: Lower energy delta-ray cutoff.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if drp is not None:
            if isinstance(drp, types.Real):
                drp = drp
            elif isinstance(drp, int) or isinstance(drp, float):
                drp = types.Real(drp)
            elif isinstance(drp, str):
                drp = types.Real.from_mcnp(drp)

        if drp is not None and not (isinstance(drp.value, types.Jump) or drp >= 0 or drp == -1):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, drp)

        self._drp: types.Real = drp
