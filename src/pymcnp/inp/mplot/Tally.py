import re

from . import _option
from ... import types


class Tally(_option.MplotOption):
    """
    Represents INP `tally` elements.
    """

    _KEYWORD = 'tally'

    _ATTRS = {
        'n': types.Integer,
    }

    _REGEX = re.compile(rf'\Atally( {types.Integer._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)

    def __init__(self, n: str | int | types.Integer = None):
        """
        Initializes `Tally`.

        Parameters:
            n: Number of current tally.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.n: types.Integer = n

    @property
    def n(self) -> types.Integer:
        """
        Number of current tally

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
            n: Number of current tally.

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

        self._n: types.Integer = n
