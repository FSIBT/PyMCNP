import re

from . import _card
from .. import types
from .. import errors


class Phys_4(_card.Card):
    """
    Represents INP `phys` elements variation #4.
    """

    _KEYWORD = 'phys'

    _ATTRS = {
        'designator': types.Designator,
        'emax': types.Real,
        'istrg': types.Integer,
        'xmunum': types.Integer,
        'xmugam': types.Real,
        'i_mcs_model': types.Integer,
        'i_int_model': types.Integer,
        'i_els_model': types.Integer,
        'efac': types.Real,
        'ckvnum': types.Real,
        'drp': types.Real,
    }

    _REGEX = re.compile(
        rf'\Aphys:(\S+)( {types.Real._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        designator: str | types.Designator,
        emax: str | int | float | types.Real = None,
        istrg: str | int | types.Integer = None,
        xmunum: str | int | types.Integer = None,
        xmugam: str | int | float | types.Real = None,
        i_mcs_model: str | int | types.Integer = None,
        i_int_model: str | int | types.Integer = None,
        i_els_model: str | int | types.Integer = None,
        efac: str | int | float | types.Real = None,
        ckvnum: str | int | float | types.Real = None,
        drp: str | int | float | types.Real = None,
    ):
        """
        Initializes `Phys_4`.

        Parameters:
            designator: Data card particle designator.
            emax: Upper energy limit.
            istrg: Charged-particle straggling controls.
            xmunum: Selection of muonic x-ray controls.
            xmugam: Probability for emitting k-shell photon.
            i_mcs_model: Choice of Coulomb scattering model controls.
            i_int_model: Treatment of nuclear interactions controls.
            i_els_model: Treatment of nuclear elastic scattering controls.
            efac: Stopping power energy spacing.
            ckvnum: Crenkov photon emission scalar.
            drp: Lower energy delta-ray cutoff.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.designator: types.Designator = designator
        self.emax: types.Real = emax
        self.istrg: types.Integer = istrg
        self.xmunum: types.Integer = xmunum
        self.xmugam: types.Real = xmugam
        self.i_mcs_model: types.Integer = i_mcs_model
        self.i_int_model: types.Integer = i_int_model
        self.i_els_model: types.Integer = i_els_model
        self.efac: types.Real = efac
        self.ckvnum: types.Real = ckvnum
        self.drp: types.Real = drp

    @property
    def designator(self) -> types.Designator:
        """
        Data card particle designator

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._designator

    @designator.setter
    def designator(self, designator: str | types.Designator) -> None:
        """
        Sets `designator`.

        Parameters:
            designator: Data card particle designator.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if designator is not None:
            if isinstance(designator, types.Designator):
                designator = designator
            elif isinstance(designator, str):
                designator = types.Designator.from_mcnp(designator)

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, designator)

        self._designator: types.Designator = designator

    @property
    def emax(self) -> types.Real:
        """
        Upper energy limit

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
            emax: Upper energy limit.

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
    def xmunum(self) -> types.Integer:
        """
        Selection of muonic x-ray controls

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._xmunum

    @xmunum.setter
    def xmunum(self, xmunum: str | int | types.Integer) -> None:
        """
        Sets `xmunum`.

        Parameters:
            xmunum: Selection of muonic x-ray controls.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if xmunum is not None:
            if isinstance(xmunum, types.Integer):
                xmunum = xmunum
            elif isinstance(xmunum, int):
                xmunum = types.Integer(xmunum)
            elif isinstance(xmunum, str):
                xmunum = types.Integer.from_mcnp(xmunum)

        if xmunum is not None and not (isinstance(xmunum.value, types.Jump) or xmunum in {-1, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, xmunum)

        self._xmunum: types.Integer = xmunum

    @property
    def xmugam(self) -> types.Real:
        """
        Probability for emitting k-shell photon

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._xmugam

    @xmugam.setter
    def xmugam(self, xmugam: str | int | float | types.Real) -> None:
        """
        Sets `xmugam`.

        Parameters:
            xmugam: Probability for emitting k-shell photon.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if xmugam is not None:
            if isinstance(xmugam, types.Real):
                xmugam = xmugam
            elif isinstance(xmugam, int) or isinstance(xmugam, float):
                xmugam = types.Real(xmugam)
            elif isinstance(xmugam, str):
                xmugam = types.Real.from_mcnp(xmugam)

        self._xmugam: types.Real = xmugam

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
