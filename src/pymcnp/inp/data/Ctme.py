import re

from . import _option
from ...utils import types
from ...utils import errors


class Ctme(_option.DataOption):
    """
    Represents INP ctme elements.

    Attributes:
        tme: maximum amount of minutes for Monte Carlo calculation.
    """

    _KEYWORD = 'ctme'

    _ATTRS = {
        'tme': types.Integer,
    }

    _REGEX = re.compile(rf'\Actme( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, tme: str | int | types.Integer):
        """
        Initializes ``Ctme``.

        Parameters:
            tme: maximum amount of minutes for Monte Carlo calculation.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.tme: types.Integer = tme

    @property
    def tme(self) -> types.Integer:
        """
        Gets ``tme``.

        Returns:
            ``tme``.
        """

        return self._tme

    @tme.setter
    def tme(self, tme: str | int | types.Integer) -> None:
        """
        Sets ``tme``.

        Parameters:
            tme: maximum amount of minutes for Monte Carlo calculation.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if tme is not None:
            if isinstance(tme, types.Integer):
                tme = tme
            elif isinstance(tme, int):
                tme = types.Integer(tme)
            elif isinstance(tme, str):
                tme = types.Integer.from_mcnp(tme)
            else:
                raise TypeError

        if tme is None or not (tme >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, tme)

        self._tme: types.Integer = tme
