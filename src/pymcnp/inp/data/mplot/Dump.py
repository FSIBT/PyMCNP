import re

from . import _option
from .... import types


class Dump(_option.MplotOption):
    """
    Represents INP dump elements.
    """

    _KEYWORD = 'dump'

    _ATTRS = {
        'n': types.Integer,
    }

    _REGEX = re.compile(rf'\Adump( {types.Integer._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)

    def __init__(self, n: str | int | types.Integer = None):
        """
        Initializes ``Dump``.

        Parameters:
            n: RUNTPE read dump number.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.n: types.Integer = n

    @property
    def n(self) -> types.Integer:
        """
        RUNTPE read dump number

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._n

    @n.setter
    def n(self, n: str | int | types.Integer) -> None:
        """
        Sets ``n``.

        Parameters:
            n: RUNTPE read dump number.

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
