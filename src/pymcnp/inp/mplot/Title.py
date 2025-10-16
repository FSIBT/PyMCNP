import re

from . import _option
from ... import types
from ... import errors


class Title(_option.MplotOption):
    """
    Represents INP `title` elements.
    """

    _KEYWORD = 'title'

    _ATTRS = {
        'n': types.Integer,
        'aa': types.String,
    }

    _REGEX = re.compile(rf'\Atitle( {types.Integer._REGEX.pattern[2:-2]})( \"{types.String._REGEX.pattern[2:-2]}\")\Z', re.IGNORECASE)

    def __init__(self, n: str | int | types.Integer, aa: str | types.String):
        """
        Initializes `Title`.

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
        Line number

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

        if n is None or not (n > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, n)

        self._n: types.Integer = n

    @property
    def aa(self) -> types.String:
        """
        Line to substitute

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._aa

    @aa.setter
    def aa(self, aa: str | types.String) -> None:
        """
        Sets `aa`.

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

        if aa is None or not (len(aa) <= 40):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, aa)

        self._aa: types.String = aa
