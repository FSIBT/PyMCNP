import re

from . import _option
from ....utils import types
from ....utils import errors


class Title(_option.MplotOption):
    """
    Represents INP title elements.

    Attributes:
        n: Line number.
        aa: Line to substitute.
    """

    _KEYWORD = 'title'

    _ATTRS = {
        'n': types.Integer,
        'aa': types.String,
    }

    _REGEX = re.compile(rf'\Atitle( {types.Integer._REGEX.pattern[2:-2]})( \"{types.String._REGEX.pattern[2:-2]}\")\Z')

    def __init__(self, n: str | int | types.Integer, aa: str | types.String):
        """
        Initializes ``Title``.

        Parameters:
            n: Line number.
            aa: Line to substitute.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.n: types.Integer = n
        self.aa: types.String = aa

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
            n: Line number.

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

        if n is None or not (n > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, n)

        self._n: types.Integer = n

    @property
    def aa(self) -> types.String:
        """
        Gets ``aa``.

        Returns:
            ``aa``.
        """

        return self._aa

    @aa.setter
    def aa(self, aa: str | types.String) -> None:
        """
        Sets ``aa``.

        Parameters:
            aa: Line to substitute.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if aa is not None:
            if isinstance(aa, types.String):
                aa = aa
            elif isinstance(aa, str):
                aa = types.String.from_mcnp(aa)
            else:
                raise TypeError

        if aa is None or not (len(aa) <= 40):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, aa)

        self._aa: types.String = aa
