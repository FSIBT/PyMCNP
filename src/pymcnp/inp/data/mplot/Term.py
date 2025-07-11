import re

from . import _option
from ....utils import types
from ....utils import errors


class Term(_option.MplotOption):
    """
    Represents INP term elements.

    Attributes:
        n: Output decive specifier.
    """

    _KEYWORD = 'term'

    _ATTRS = {
        'n': types.Integer,
    }

    _REGEX = re.compile(rf'\Aterm( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, n: str | int | types.Integer):
        """
        Initializes ``Term``.

        Parameters:
            n: Output decive specifier.

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
            n: Output decive specifier.

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

        if n is None or n not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, n)

        self._n: types.Integer = n
