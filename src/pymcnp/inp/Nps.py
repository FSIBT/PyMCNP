import re

from . import _card
from .. import types
from .. import errors


class Nps(_card.Card):
    """
    Represents INP `nps` cards.
    """

    _KEYWORD = 'nps'

    _ATTRS = {
        'npp': types.Integer,
        'npsmg': types.Integer,
    }

    _REGEX = re.compile(rf'\Anps( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)

    def __init__(self, npp: str | int | types.Integer, npsmg: str | int | types.Integer = None):
        """
        Initializes `Nps`.

        Parameters:
            npp: Total number of histories to run.
            npsmg: Number of history with direct source contributions.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.npp: types.Integer = npp
        self.npsmg: types.Integer = npsmg

    @property
    def npp(self) -> types.Integer:
        """
        Total number of histories to run

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._npp

    @npp.setter
    def npp(self, npp: str | int | types.Integer) -> None:
        """
        Sets `npp`.

        Parameters:
            npp: Total number of histories to run.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if npp is not None:
            if isinstance(npp, types.Integer):
                npp = npp
            elif isinstance(npp, int):
                npp = types.Integer(npp)
            elif isinstance(npp, str):
                npp = types.Integer.from_mcnp(npp)

        if npp is None or not (npp > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, npp)

        self._npp: types.Integer = npp

    @property
    def npsmg(self) -> types.Integer:
        """
        Number of history with direct source contributions

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._npsmg

    @npsmg.setter
    def npsmg(self, npsmg: str | int | types.Integer) -> None:
        """
        Sets `npsmg`.

        Parameters:
            npsmg: Number of history with direct source contributions.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if npsmg is not None:
            if isinstance(npsmg, types.Integer):
                npsmg = npsmg
            elif isinstance(npsmg, int):
                npsmg = types.Integer(npsmg)
            elif isinstance(npsmg, str):
                npsmg = types.Integer.from_mcnp(npsmg)

        if npsmg is not None and not (npsmg > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, npsmg)

        self._npsmg: types.Integer = npsmg
