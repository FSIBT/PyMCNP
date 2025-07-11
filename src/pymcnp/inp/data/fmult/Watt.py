import re

from . import _option
from ....utils import types
from ....utils import errors


class Watt(_option.FmultOption):
    """
    Represents INP watt elements.

    Attributes:
        a: Watt energy spectrum parameters a.
        b: Watt energy spectrum parameters b.
    """

    _KEYWORD = 'watt'

    _ATTRS = {
        'a': types.Real,
        'b': types.Real,
    }

    _REGEX = re.compile(rf'\Awatt( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, a: str | int | float | types.Real, b: str | int | float | types.Real):
        """
        Initializes ``Watt``.

        Parameters:
            a: Watt energy spectrum parameters a.
            b: Watt energy spectrum parameters b.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.a: types.Real = a
        self.b: types.Real = b

    @property
    def a(self) -> types.Real:
        """
        Gets ``a``.

        Returns:
            ``a``.
        """

        return self._a

    @a.setter
    def a(self, a: str | int | float | types.Real) -> None:
        """
        Sets ``a``.

        Parameters:
            a: Watt energy spectrum parameters a.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if a is not None:
            if isinstance(a, types.Real):
                a = a
            elif isinstance(a, int):
                a = types.Real(a)
            elif isinstance(a, float):
                a = types.Real(a)
            elif isinstance(a, str):
                a = types.Real.from_mcnp(a)
            else:
                raise TypeError

        if a is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a)

        self._a: types.Real = a

    @property
    def b(self) -> types.Real:
        """
        Gets ``b``.

        Returns:
            ``b``.
        """

        return self._b

    @b.setter
    def b(self, b: str | int | float | types.Real) -> None:
        """
        Sets ``b``.

        Parameters:
            b: Watt energy spectrum parameters b.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if b is not None:
            if isinstance(b, types.Real):
                b = b
            elif isinstance(b, int):
                b = types.Real(b)
            elif isinstance(b, float):
                b = types.Real(b)
            elif isinstance(b, str):
                b = types.Real.from_mcnp(b)
            else:
                raise TypeError

        if b is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, b)

        self._b: types.Real = b
