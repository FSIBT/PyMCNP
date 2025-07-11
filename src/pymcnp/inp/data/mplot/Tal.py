import re

from . import _option
from ....utils import types
from ....utils import errors


class Tal(_option.MplotOption):
    """
    Represents INP tal elements.

    Attributes:
        n: Tally number.
    """

    _KEYWORD = 'tal'

    _ATTRS = {
        'n': types.Integer,
    }

    _REGEX = re.compile(rf'\Atal( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, n: str | int | types.Integer):
        """
        Initializes ``Tal``.

        Parameters:
            n: Tally number.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.n: types.Integer = n

    @property
    def n(self) -> types.Integer:
        """
        Gets ``n``.

        Returns:
            ``n``.
        """

        return self._n

    @n.setter
    def n(self, n: str | int | types.Integer) -> None:
        """
        Sets ``n``.

        Parameters:
            n: Tally number.

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
            else:
                raise TypeError

        if n is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, n)

        self._n: types.Integer = n
