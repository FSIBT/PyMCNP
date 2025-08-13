import re

from . import _card
from .. import types


class Prdmp(_card.Card):
    """
    Represents INP `prdmp` cards.
    """

    _KEYWORD = 'prdmp'

    _ATTRS = {
        'ndp': types.Integer,
        'ndm': types.Integer,
        'mct': types.Integer,
        'ndmp': types.Integer,
        'dmmp': types.Integer,
    }

    _REGEX = re.compile(
        rf'\Aprdmp( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        ndp: str | int | types.Integer = None,
        ndm: str | int | types.Integer = None,
        mct: str | int | types.Integer = None,
        ndmp: str | int | types.Integer = None,
        dmmp: str | int | types.Integer = None,
    ):
        """
        Initializes `Prdmp`.

        Parameters:
            ndp: Increment for printing tallies.
            ndm: Increment for dumping to RUNTPE file.
            mct: Controls printing of MCTAL file.
            ndmp: Maximum number of dumps on RUNTPE file.
            dmmp: Controls frequently of tally fluctuation chart.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.ndp: types.Integer = ndp
        self.ndm: types.Integer = ndm
        self.mct: types.Integer = mct
        self.ndmp: types.Integer = ndmp
        self.dmmp: types.Integer = dmmp

    @property
    def ndp(self) -> types.Integer:
        """
        Increment for printing tallies

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ndp

    @ndp.setter
    def ndp(self, ndp: str | int | types.Integer) -> None:
        """
        Sets `ndp`.

        Parameters:
            ndp: Increment for printing tallies.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ndp is not None:
            if isinstance(ndp, types.Integer):
                ndp = ndp
            elif isinstance(ndp, int):
                ndp = types.Integer(ndp)
            elif isinstance(ndp, str):
                ndp = types.Integer.from_mcnp(ndp)

        self._ndp: types.Integer = ndp

    @property
    def ndm(self) -> types.Integer:
        """
        Increment for dumping to RUNTPE file

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ndm

    @ndm.setter
    def ndm(self, ndm: str | int | types.Integer) -> None:
        """
        Sets `ndm`.

        Parameters:
            ndm: Increment for dumping to RUNTPE file.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ndm is not None:
            if isinstance(ndm, types.Integer):
                ndm = ndm
            elif isinstance(ndm, int):
                ndm = types.Integer(ndm)
            elif isinstance(ndm, str):
                ndm = types.Integer.from_mcnp(ndm)

        self._ndm: types.Integer = ndm

    @property
    def mct(self) -> types.Integer:
        """
        Controls printing of MCTAL file

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._mct

    @mct.setter
    def mct(self, mct: str | int | types.Integer) -> None:
        """
        Sets `mct`.

        Parameters:
            mct: Controls printing of MCTAL file.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if mct is not None:
            if isinstance(mct, types.Integer):
                mct = mct
            elif isinstance(mct, int):
                mct = types.Integer(mct)
            elif isinstance(mct, str):
                mct = types.Integer.from_mcnp(mct)

        self._mct: types.Integer = mct

    @property
    def ndmp(self) -> types.Integer:
        """
        Maximum number of dumps on RUNTPE file

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ndmp

    @ndmp.setter
    def ndmp(self, ndmp: str | int | types.Integer) -> None:
        """
        Sets `ndmp`.

        Parameters:
            ndmp: Maximum number of dumps on RUNTPE file.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ndmp is not None:
            if isinstance(ndmp, types.Integer):
                ndmp = ndmp
            elif isinstance(ndmp, int):
                ndmp = types.Integer(ndmp)
            elif isinstance(ndmp, str):
                ndmp = types.Integer.from_mcnp(ndmp)

        self._ndmp: types.Integer = ndmp

    @property
    def dmmp(self) -> types.Integer:
        """
        Controls frequently of tally fluctuation chart

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._dmmp

    @dmmp.setter
    def dmmp(self, dmmp: str | int | types.Integer) -> None:
        """
        Sets `dmmp`.

        Parameters:
            dmmp: Controls frequently of tally fluctuation chart.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if dmmp is not None:
            if isinstance(dmmp, types.Integer):
                dmmp = dmmp
            elif isinstance(dmmp, int):
                dmmp = types.Integer(dmmp)
            elif isinstance(dmmp, str):
                dmmp = types.Integer.from_mcnp(dmmp)

        self._dmmp: types.Integer = dmmp
