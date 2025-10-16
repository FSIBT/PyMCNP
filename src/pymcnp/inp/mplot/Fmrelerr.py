import re

from . import _option
from ... import types
from ... import errors


class Fmrelerr(_option.MplotOption):
    """
    Represents INP `fmrelerr` elements.
    """

    _KEYWORD = 'fmrelerr'

    _ATTRS = {
        'n': types.Integer,
    }

    _REGEX = re.compile(rf'\Afmrelerr( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, n: str | int | types.Integer):
        """
        Initializes `Fmrelerr`.

        Parameters:
            n: Tally error to plot.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.n: types.Integer = n

    @property
    def n(self) -> types.Integer:
        """
        Tally error to plot

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._n

    @n.setter
    def n(self, n: str | int | types.Integer) -> None:
        """
        Sets `n`.

        Parameters:
            n: Tally error to plot.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if n is not None:
            if isinstance(n, types.Integer):
                n = n
            elif isinstance(n, int):
                n = types.Integer(n)
            elif isinstance(n, str):
                n = types.Integer.from_mcnp(n)

        if n is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, n)

        self._n: types.Integer = n
