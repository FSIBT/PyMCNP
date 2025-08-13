import re

from . import _card
from .. import types
from .. import errors


class Kcode(_card.Card):
    """
    Represents INP `kcode` cards.
    """

    _KEYWORD = 'kcode'

    _ATTRS = {
        'nsrck': types.Integer,
        'rkk': types.Real,
        'ikz': types.Integer,
        'kct': types.Integer,
        'msrk': types.Integer,
        'knrm': types.Integer,
        'mrkp': types.Integer,
        'kc8': types.Integer,
    }

    _REGEX = re.compile(
        rf'\Akcode( {types.Integer._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        nsrck: str | int | types.Integer = None,
        rkk: str | int | float | types.Real = None,
        ikz: str | int | types.Integer = None,
        kct: str | int | types.Integer = None,
        msrk: str | int | types.Integer = None,
        knrm: str | int | types.Integer = None,
        mrkp: str | int | types.Integer = None,
        kc8: str | int | types.Integer = None,
    ):
        """
        Initializes `Kcode`.

        Parameters:
            nsrck: Number of source histories per cycle.
            rkk: Initial guess of keff.
            ikz: Number of cycles to be skipped before beginning tally accumulation.
            kct: Total number of cycles to be done.
            msrk: Number of source points to allocate for.
            knrm: Normalization of tallies setting.
            mrkp: Maximum number of cycle values on MCTAL or RUNTPE files.
            kc8: Number of cylces for average setting.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.nsrck: types.Integer = nsrck
        self.rkk: types.Real = rkk
        self.ikz: types.Integer = ikz
        self.kct: types.Integer = kct
        self.msrk: types.Integer = msrk
        self.knrm: types.Integer = knrm
        self.mrkp: types.Integer = mrkp
        self.kc8: types.Integer = kc8

    @property
    def nsrck(self) -> types.Integer:
        """
        Number of source histories per cycle

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._nsrck

    @nsrck.setter
    def nsrck(self, nsrck: str | int | types.Integer) -> None:
        """
        Sets `nsrck`.

        Parameters:
            nsrck: Number of source histories per cycle.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if nsrck is not None:
            if isinstance(nsrck, types.Integer):
                nsrck = nsrck
            elif isinstance(nsrck, int):
                nsrck = types.Integer(nsrck)
            elif isinstance(nsrck, str):
                nsrck = types.Integer.from_mcnp(nsrck)

        if nsrck is not None and not (isinstance(nsrck.value, types.Jump) or nsrck >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, nsrck)

        self._nsrck: types.Integer = nsrck

    @property
    def rkk(self) -> types.Real:
        """
        Initial guess of keff

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._rkk

    @rkk.setter
    def rkk(self, rkk: str | int | float | types.Real) -> None:
        """
        Sets `rkk`.

        Parameters:
            rkk: Initial guess of keff.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if rkk is not None:
            if isinstance(rkk, types.Real):
                rkk = rkk
            elif isinstance(rkk, int) or isinstance(rkk, float):
                rkk = types.Real(rkk)
            elif isinstance(rkk, str):
                rkk = types.Real.from_mcnp(rkk)

        self._rkk: types.Real = rkk

    @property
    def ikz(self) -> types.Integer:
        """
        Number of cycles to be skipped before beginning tally accumulation

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ikz

    @ikz.setter
    def ikz(self, ikz: str | int | types.Integer) -> None:
        """
        Sets `ikz`.

        Parameters:
            ikz: Number of cycles to be skipped before beginning tally accumulation.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ikz is not None:
            if isinstance(ikz, types.Integer):
                ikz = ikz
            elif isinstance(ikz, int):
                ikz = types.Integer(ikz)
            elif isinstance(ikz, str):
                ikz = types.Integer.from_mcnp(ikz)

        self._ikz: types.Integer = ikz

    @property
    def kct(self) -> types.Integer:
        """
        Total number of cycles to be done

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._kct

    @kct.setter
    def kct(self, kct: str | int | types.Integer) -> None:
        """
        Sets `kct`.

        Parameters:
            kct: Total number of cycles to be done.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if kct is not None:
            if isinstance(kct, types.Integer):
                kct = kct
            elif isinstance(kct, int):
                kct = types.Integer(kct)
            elif isinstance(kct, str):
                kct = types.Integer.from_mcnp(kct)

        if kct is not None and not (isinstance(kct.value, types.Jump) or kct > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, kct)

        self._kct: types.Integer = kct

    @property
    def msrk(self) -> types.Integer:
        """
        Number of source points to allocate for

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._msrk

    @msrk.setter
    def msrk(self, msrk: str | int | types.Integer) -> None:
        """
        Sets `msrk`.

        Parameters:
            msrk: Number of source points to allocate for.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if msrk is not None:
            if isinstance(msrk, types.Integer):
                msrk = msrk
            elif isinstance(msrk, int):
                msrk = types.Integer(msrk)
            elif isinstance(msrk, str):
                msrk = types.Integer.from_mcnp(msrk)

        if msrk is not None and not (isinstance(msrk.value, types.Jump) or msrk < 40 * (1000 if not self.nsrck or isinstance(self.nsrck.value, types.Jump) else self.nsrck)):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, msrk)

        self._msrk: types.Integer = msrk

    @property
    def knrm(self) -> types.Integer:
        """
        Normalization of tallies setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._knrm

    @knrm.setter
    def knrm(self, knrm: str | int | types.Integer) -> None:
        """
        Sets `knrm`.

        Parameters:
            knrm: Normalization of tallies setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if knrm is not None:
            if isinstance(knrm, types.Integer):
                knrm = knrm
            elif isinstance(knrm, int):
                knrm = types.Integer(knrm)
            elif isinstance(knrm, str):
                knrm = types.Integer.from_mcnp(knrm)

        if knrm is not None and not (isinstance(knrm.value, types.Jump) or knrm in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, knrm)

        self._knrm: types.Integer = knrm

    @property
    def mrkp(self) -> types.Integer:
        """
        Maximum number of cycle values on MCTAL or RUNTPE files

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._mrkp

    @mrkp.setter
    def mrkp(self, mrkp: str | int | types.Integer) -> None:
        """
        Sets `mrkp`.

        Parameters:
            mrkp: Maximum number of cycle values on MCTAL or RUNTPE files.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if mrkp is not None:
            if isinstance(mrkp, types.Integer):
                mrkp = mrkp
            elif isinstance(mrkp, int):
                mrkp = types.Integer(mrkp)
            elif isinstance(mrkp, str):
                mrkp = types.Integer.from_mcnp(mrkp)

        if mrkp is not None and not (isinstance(mrkp.value, types.Jump) or mrkp > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, mrkp)

        self._mrkp: types.Integer = mrkp

    @property
    def kc8(self) -> types.Integer:
        """
        Number of cylces for average setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._kc8

    @kc8.setter
    def kc8(self, kc8: str | int | types.Integer) -> None:
        """
        Sets `kc8`.

        Parameters:
            kc8: Number of cylces for average setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if kc8 is not None:
            if isinstance(kc8, types.Integer):
                kc8 = kc8
            elif isinstance(kc8, int):
                kc8 = types.Integer(kc8)
            elif isinstance(kc8, str):
                kc8 = types.Integer.from_mcnp(kc8)

        if kc8 is not None and not (isinstance(kc8.value, types.Jump) or kc8 in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, kc8)

        self._kc8: types.Integer = kc8
