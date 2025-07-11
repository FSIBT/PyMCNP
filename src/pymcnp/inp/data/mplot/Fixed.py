import re

from . import _option
from ....utils import types
from ....utils import errors


class Fixed(_option.MplotOption):
    """
    Represents INP fixed elements.

    Attributes:
        q: Fixed variable.
        n: Bin number.
    """

    _KEYWORD = 'fixed'

    _ATTRS = {
        'q': types.String,
        'n': types.Integer,
    }

    _REGEX = re.compile(rf'\Afixed( {types.String._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, q: str | types.String, n: str | int | types.Integer):
        """
        Initializes ``Fixed``.

        Parameters:
            q: Fixed variable.
            n: Bin number.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.q: types.String = q
        self.n: types.Integer = n

    @property
    def q(self) -> types.String:
        """
        Gets ``q``.

        Returns:
            ``q``.
        """

        return self._q

    @q.setter
    def q(self, q: str | types.String) -> None:
        """
        Sets ``q``.

        Parameters:
            q: Fixed variable.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if q is not None:
            if isinstance(q, types.String):
                q = q
            elif isinstance(q, str):
                q = types.String.from_mcnp(q)
            else:
                raise TypeError

        if q is None or q not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't', 'i', 'j', 'k'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, q)

        self._q: types.String = q

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
            n: Bin number.

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
