import re

from . import _card
from .. import types
from .. import errors


class Mgopt(_card.Card):
    """
    Represents INP `mgopt` cards.
    """

    _KEYWORD = 'mgopt'

    _ATTRS = {
        'mcal': types.String,
        'igm': types.Integer,
        'iplt': types.Integer,
        'iab': types.Integer,
        'icw': types.Integer,
        'fnw': types.Real,
        'rim': types.Real,
    }

    _REGEX = re.compile(
        rf'\Amgopt( {types.String._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        mcal: str | types.String,
        igm: str | int | types.Integer,
        iplt: str | int | types.Integer = None,
        iab: str | int | types.Integer = None,
        icw: str | int | types.Integer = None,
        fnw: str | int | float | types.Real = None,
        rim: str | int | float | types.Real = None,
    ):
        """
        Initializes `Mgopt`.

        Parameters:
            mcal: Problem type setting.
            igm: Total number of energy groups for all kinds of particle.
            iplt: Weight windows usage indicator.
            iab: Adjoint biasing for adjoint problems contorls.
            icw: Name of the reference cell for generated weight windows.
            fnw: Normalization value for generated weight windows.
            rim: Generated weight windows compression limit.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.mcal: types.String = mcal
        self.igm: types.Integer = igm
        self.iplt: types.Integer = iplt
        self.iab: types.Integer = iab
        self.icw: types.Integer = icw
        self.fnw: types.Real = fnw
        self.rim: types.Real = rim

    @property
    def mcal(self) -> types.String:
        """
        Problem type setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._mcal

    @mcal.setter
    def mcal(self, mcal: str | types.String) -> None:
        """
        Sets `mcal`.

        Parameters:
            mcal: Problem type setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if mcal is not None:
            if isinstance(mcal, types.String):
                mcal = mcal
            elif isinstance(mcal, str):
                mcal = types.String.from_mcnp(mcal)

        if mcal is None or mcal.value.lower() not in {'f', 'a'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, mcal)

        self._mcal: types.String = mcal

    @property
    def igm(self) -> types.Integer:
        """
        Total number of energy groups for all kinds of particle

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._igm

    @igm.setter
    def igm(self, igm: str | int | types.Integer) -> None:
        """
        Sets `igm`.

        Parameters:
            igm: Total number of energy groups for all kinds of particle.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if igm is not None:
            if isinstance(igm, types.Integer):
                igm = igm
            elif isinstance(igm, int):
                igm = types.Integer(igm)
            elif isinstance(igm, str):
                igm = types.Integer.from_mcnp(igm)

        if igm is None or not (igm >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, igm)

        self._igm: types.Integer = igm

    @property
    def iplt(self) -> types.Integer:
        """
        Weight windows usage indicator

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._iplt

    @iplt.setter
    def iplt(self, iplt: str | int | types.Integer) -> None:
        """
        Sets `iplt`.

        Parameters:
            iplt: Weight windows usage indicator.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if iplt is not None:
            if isinstance(iplt, types.Integer):
                iplt = iplt
            elif isinstance(iplt, int):
                iplt = types.Integer(iplt)
            elif isinstance(iplt, str):
                iplt = types.Integer.from_mcnp(iplt)

        if iplt is not None and iplt not in {0, 1, 2}:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, iplt)

        self._iplt: types.Integer = iplt

    @property
    def iab(self) -> types.Integer:
        """
        Adjoint biasing for adjoint problems contorls

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._iab

    @iab.setter
    def iab(self, iab: str | int | types.Integer) -> None:
        """
        Sets `iab`.

        Parameters:
            iab: Adjoint biasing for adjoint problems contorls.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if iab is not None:
            if isinstance(iab, types.Integer):
                iab = iab
            elif isinstance(iab, int):
                iab = types.Integer(iab)
            elif isinstance(iab, str):
                iab = types.Integer.from_mcnp(iab)

        if iab is not None and iab not in {0, 1, 2}:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, iab)

        self._iab: types.Integer = iab

    @property
    def icw(self) -> types.Integer:
        """
        Name of the reference cell for generated weight windows

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._icw

    @icw.setter
    def icw(self, icw: str | int | types.Integer) -> None:
        """
        Sets `icw`.

        Parameters:
            icw: Name of the reference cell for generated weight windows.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if icw is not None:
            if isinstance(icw, types.Integer):
                icw = icw
            elif isinstance(icw, int):
                icw = types.Integer(icw)
            elif isinstance(icw, str):
                icw = types.Integer.from_mcnp(icw)

        self._icw: types.Integer = icw

    @property
    def fnw(self) -> types.Real:
        """
        Normalization value for generated weight windows

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._fnw

    @fnw.setter
    def fnw(self, fnw: str | int | float | types.Real) -> None:
        """
        Sets `fnw`.

        Parameters:
            fnw: Normalization value for generated weight windows.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if fnw is not None:
            if isinstance(fnw, types.Real):
                fnw = fnw
            elif isinstance(fnw, int) or isinstance(fnw, float):
                fnw = types.Real(fnw)
            elif isinstance(fnw, str):
                fnw = types.Real.from_mcnp(fnw)

        self._fnw: types.Real = fnw

    @property
    def rim(self) -> types.Real:
        """
        Generated weight windows compression limit

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._rim

    @rim.setter
    def rim(self, rim: str | int | float | types.Real) -> None:
        """
        Sets `rim`.

        Parameters:
            rim: Generated weight windows compression limit.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if rim is not None:
            if isinstance(rim, types.Real):
                rim = rim
            elif isinstance(rim, int) or isinstance(rim, float):
                rim = types.Real(rim)
            elif isinstance(rim, str):
                rim = types.Real.from_mcnp(rim)

        self._rim: types.Real = rim
