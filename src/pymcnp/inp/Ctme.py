import re

from . import _card
from .. import types
from .. import errors


class Ctme(_card.Card):
    """
    Represents INP ctme cards.
    """

    _KEYWORD = 'ctme'

    _ATTRS = {
        'tme': types.Integer,
    }

    _REGEX = re.compile(rf'\Actme( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, tme: str | int | types.Integer):
        """
        Initializes `Ctme`.

        Parameters:
            tme: maximum amount of minutes for Monte Carlo calculation.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.tme: types.Integer = tme

    @property
    def tme(self) -> types.Integer:
        """
        Maximum amount of minutes for Monte Carlo calculation

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._tme

    @tme.setter
    def tme(self, tme: str | int | types.Integer) -> None:
        """
        Sets `tme`.

        Parameters:
            tme: maximum amount of minutes for Monte Carlo calculation.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if tme is not None:
            if isinstance(tme, types.Integer):
                tme = tme
            elif isinstance(tme, int):
                tme = types.Integer(tme)
            elif isinstance(tme, str):
                tme = types.Integer.from_mcnp(tme)

        if tme is None or not (tme >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, tme)

        self._tme: types.Integer = tme
