import re

from . import _card
from .. import types
from .. import errors


class Wwp(_card.Card):
    """
    Represents INP `wwp` cards.
    """

    _KEYWORD = 'wwp'

    _ATTRS = {
        'designator': types.Designator,
        'wupn': types.Real,
        'wsurvn': types.Real,
        'mxspln': types.Real,
        'mwhere': types.Integer,
        'switchn': types.Real,
        'mtime': types.Integer,
        'wnrom': types.Real,
        'etsplt': types.Integer,
        'wu': types.Real,
        'nmfp': types.Real,
    }

    _REGEX = re.compile(
        rf'\Awwp:(\S+)( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        designator: str | types.Designator,
        wupn: str | int | float | types.Real = None,
        wsurvn: str | int | float | types.Real = None,
        mxspln: str | int | float | types.Real = None,
        mwhere: str | int | types.Integer = None,
        switchn: str | int | float | types.Real = None,
        mtime: str | int | types.Integer = None,
        wnrom: str | int | float | types.Real = None,
        etsplt: str | int | types.Integer = None,
        wu: str | int | float | types.Real = None,
        nmfp: str | int | float | types.Real = None,
    ):
        """
        Initializes `Wwp`.

        Parameters:
            designator: Data card particle designator.
            wupn: Multiplier to define the weight window upper limit.
            wsurvn: Multiplier to define the maximum Russian roulette survival weight within the window.
            mxspln: Maximum number of integer splits.
            mwhere: Controls where to check a particle’s weight.
            switchn: Controls where to get the lower weight-window bounds.
            mtime: Energy/time-dependent window setting.
            wnrom: Weight-window normalization factor.
            etsplt: ESLPT & TSPLT split/roulette on/off.
            wu: Limits the maximum lower weight-window bound for any particle, energy, or time.
            nmfp: Limits the maximum lower weight-window bound for any particle, energy, or time.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.designator: types.Designator = designator
        self.wupn: types.Real = wupn
        self.wsurvn: types.Real = wsurvn
        self.mxspln: types.Real = mxspln
        self.mwhere: types.Integer = mwhere
        self.switchn: types.Real = switchn
        self.mtime: types.Integer = mtime
        self.wnrom: types.Real = wnrom
        self.etsplt: types.Integer = etsplt
        self.wu: types.Real = wu
        self.nmfp: types.Real = nmfp

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
    def wupn(self) -> types.Real:
        """
        Multiplier to define the weight window upper limit

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._wupn

    @wupn.setter
    def wupn(self, wupn: str | int | float | types.Real) -> None:
        """
        Sets `wupn`.

        Parameters:
            wupn: Multiplier to define the weight window upper limit.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if wupn is not None:
            if isinstance(wupn, types.Real):
                wupn = wupn
            elif isinstance(wupn, int) or isinstance(wupn, float):
                wupn = types.Real(wupn)
            elif isinstance(wupn, str):
                wupn = types.Real.from_mcnp(wupn)

        if wupn is not None and not (isinstance(wupn.value, types.Jump) or wupn >= 2):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, wupn)

        self._wupn: types.Real = wupn

    @property
    def wsurvn(self) -> types.Real:
        """
        Multiplier to define the maximum Russian roulette survival weight within the window

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._wsurvn

    @wsurvn.setter
    def wsurvn(self, wsurvn: str | int | float | types.Real) -> None:
        """
        Sets `wsurvn`.

        Parameters:
            wsurvn: Multiplier to define the maximum Russian roulette survival weight within the window.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if wsurvn is not None:
            if isinstance(wsurvn, types.Real):
                wsurvn = wsurvn
            elif isinstance(wsurvn, int) or isinstance(wsurvn, float):
                wsurvn = types.Real(wsurvn)
            elif isinstance(wsurvn, str):
                wsurvn = types.Real.from_mcnp(wsurvn)

        if wsurvn is not None and not (isinstance(wsurvn.value, types.Jump) or 1 < wsurvn):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, wsurvn)

        self._wsurvn: types.Real = wsurvn

    @property
    def mxspln(self) -> types.Real:
        """
        Maximum number of integer splits

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._mxspln

    @mxspln.setter
    def mxspln(self, mxspln: str | int | float | types.Real) -> None:
        """
        Sets `mxspln`.

        Parameters:
            mxspln: Maximum number of integer splits.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if mxspln is not None:
            if isinstance(mxspln, types.Real):
                mxspln = mxspln
            elif isinstance(mxspln, int) or isinstance(mxspln, float):
                mxspln = types.Real(mxspln)
            elif isinstance(mxspln, str):
                mxspln = types.Real.from_mcnp(mxspln)

        if mxspln is not None and not (isinstance(mxspln.value, types.Jump) or 1 < mxspln):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, mxspln)

        self._mxspln: types.Real = mxspln

    @property
    def mwhere(self) -> types.Integer:
        """
        Controls where to check a particle’s weight

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._mwhere

    @mwhere.setter
    def mwhere(self, mwhere: str | int | types.Integer) -> None:
        """
        Sets `mwhere`.

        Parameters:
            mwhere: Controls where to check a particle’s weight.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if mwhere is not None:
            if isinstance(mwhere, types.Integer):
                mwhere = mwhere
            elif isinstance(mwhere, int):
                mwhere = types.Integer(mwhere)
            elif isinstance(mwhere, str):
                mwhere = types.Integer.from_mcnp(mwhere)

        if mwhere is not None and not (isinstance(mwhere.value, types.Jump) or mwhere in {-1, 0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, mwhere)

        self._mwhere: types.Integer = mwhere

    @property
    def switchn(self) -> types.Real:
        """
        Controls where to get the lower weight-window bounds

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._switchn

    @switchn.setter
    def switchn(self, switchn: str | int | float | types.Real) -> None:
        """
        Sets `switchn`.

        Parameters:
            switchn: Controls where to get the lower weight-window bounds.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if switchn is not None:
            if isinstance(switchn, types.Real):
                switchn = switchn
            elif isinstance(switchn, int) or isinstance(switchn, float):
                switchn = types.Real(switchn)
            elif isinstance(switchn, str):
                switchn = types.Real.from_mcnp(switchn)

        self._switchn: types.Real = switchn

    @property
    def mtime(self) -> types.Integer:
        """
        Energy/time-dependent window setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._mtime

    @mtime.setter
    def mtime(self, mtime: str | int | types.Integer) -> None:
        """
        Sets `mtime`.

        Parameters:
            mtime: Energy/time-dependent window setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if mtime is not None:
            if isinstance(mtime, types.Integer):
                mtime = mtime
            elif isinstance(mtime, int):
                mtime = types.Integer(mtime)
            elif isinstance(mtime, str):
                mtime = types.Integer.from_mcnp(mtime)

        self._mtime: types.Integer = mtime

    @property
    def wnrom(self) -> types.Real:
        """
        Weight-window normalization factor

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._wnrom

    @wnrom.setter
    def wnrom(self, wnrom: str | int | float | types.Real) -> None:
        """
        Sets `wnrom`.

        Parameters:
            wnrom: Weight-window normalization factor.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if wnrom is not None:
            if isinstance(wnrom, types.Real):
                wnrom = wnrom
            elif isinstance(wnrom, int) or isinstance(wnrom, float):
                wnrom = types.Real(wnrom)
            elif isinstance(wnrom, str):
                wnrom = types.Real.from_mcnp(wnrom)

        self._wnrom: types.Real = wnrom

    @property
    def etsplt(self) -> types.Integer:
        """
        ESLPT & TSPLT split/roulette on/off

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._etsplt

    @etsplt.setter
    def etsplt(self, etsplt: str | int | types.Integer) -> None:
        """
        Sets `etsplt`.

        Parameters:
            etsplt: ESLPT & TSPLT split/roulette on/off.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if etsplt is not None:
            if isinstance(etsplt, types.Integer):
                etsplt = etsplt
            elif isinstance(etsplt, int):
                etsplt = types.Integer(etsplt)
            elif isinstance(etsplt, str):
                etsplt = types.Integer.from_mcnp(etsplt)

        if etsplt is not None and not (isinstance(etsplt.value, types.Jump) or etsplt in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, etsplt)

        self._etsplt: types.Integer = etsplt

    @property
    def wu(self) -> types.Real:
        """
        Limits the maximum lower weight-window bound for any particle, energy, or time

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._wu

    @wu.setter
    def wu(self, wu: str | int | float | types.Real) -> None:
        """
        Sets `wu`.

        Parameters:
            wu: Limits the maximum lower weight-window bound for any particle, energy, or time.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if wu is not None:
            if isinstance(wu, types.Real):
                wu = wu
            elif isinstance(wu, int) or isinstance(wu, float):
                wu = types.Real(wu)
            elif isinstance(wu, str):
                wu = types.Real.from_mcnp(wu)

        self._wu: types.Real = wu

    @property
    def nmfp(self) -> types.Real:
        """
        Limits the maximum lower weight-window bound for any particle, energy, or time

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._nmfp

    @nmfp.setter
    def nmfp(self, nmfp: str | int | float | types.Real) -> None:
        """
        Sets `nmfp`.

        Parameters:
            nmfp: Limits the maximum lower weight-window bound for any particle, energy, or time.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if nmfp is not None:
            if isinstance(nmfp, types.Real):
                nmfp = nmfp
            elif isinstance(nmfp, int) or isinstance(nmfp, float):
                nmfp = types.Real(nmfp)
            elif isinstance(nmfp, str):
                nmfp = types.Real.from_mcnp(nmfp)

        self._nmfp: types.Real = nmfp
