import re

from . import _option
from ...utils import types
from ...utils import errors


class Sp_1(_option.DataOption):
    """
    Represents INP sp variation #1 elements.

    Attributes:
        function: Built-in function designator.
        a: Built-in function parameter #1.
        b: Built-in function parameter #2.
    """

    _KEYWORD = 'sp'

    _ATTRS = {
        'function': types.Integer,
        'a': types.Real,
        'b': types.Real,
    }

    _REGEX = re.compile(rf'\Asp( {types.Integer._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?\Z')

    def __init__(self, function: str | int | types.Integer, a: str | int | float | types.Real, b: str | int | float | types.Real = None):
        """
        Initializes ``Sp_1``.

        Parameters:
            function: Built-in function designator.
            a: Built-in function parameter #1.
            b: Built-in function parameter #2.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.function: types.Integer = function
        self.a: types.Real = a
        self.b: types.Real = b

    @property
    def function(self) -> types.Integer:
        """
        Gets ``function``.

        Returns:
            ``function``.
        """

        return self._function

    @function.setter
    def function(self, function: str | int | types.Integer) -> None:
        """
        Sets ``function``.

        Parameters:
            function: Built-in function designator.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if function is not None:
            if isinstance(function, types.Integer):
                function = function
            elif isinstance(function, int):
                function = types.Integer(function)
            elif isinstance(function, str):
                function = types.Integer.from_mcnp(function)
            else:
                raise TypeError

        if function is None or function not in {-2, -3, -4, -5, -6, -7, -21, -31, -41}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, function)

        self._function: types.Integer = function

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
            a: Built-in function parameter #1.

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
            b: Built-in function parameter #2.

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

        self._b: types.Real = b
