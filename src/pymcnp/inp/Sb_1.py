import re

from . import _card
from .. import types
from .. import errors


class Sb_1(_card.Card):
    """
    Represents INP `sb` elements variation #1.
    """

    _KEYWORD = 'sb'

    _ATTRS = {
        'function': types.Integer,
        'a': types.Real,
        'b': types.Real,
    }

    _REGEX = re.compile(rf'\Asb( {types.Integer._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)

    def __init__(self, function: str | int | types.Integer, a: str | int | float | types.Real, b: str | int | float | types.Real = None):
        """
        Initializes `Sb_1`.

        Parameters:
            function: Built-in function designator.
            a: Built-in function parameter #1.
            b: Built-in function parameter #2.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.function: types.Integer = function
        self.a: types.Real = a
        self.b: types.Real = b

    @property
    def function(self) -> types.Integer:
        """
        Built-in function designator

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._function

    @function.setter
    def function(self, function: str | int | types.Integer) -> None:
        """
        Sets `function`.

        Parameters:
            function: Built-in function designator.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if function is not None:
            if isinstance(function, types.Integer):
                function = function
            elif isinstance(function, int):
                function = types.Integer(function)
            elif isinstance(function, str):
                function = types.Integer.from_mcnp(function)

        if function is None or function not in {-2, -3, -4, -5, -6, -7, -21, -31, -41}:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, function)

        self._function: types.Integer = function

    @property
    def a(self) -> types.Real:
        """
        Built-in function parameter #1

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._a

    @a.setter
    def a(self, a: str | int | float | types.Real) -> None:
        """
        Sets `a`.

        Parameters:
            a: Built-in function parameter #1.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if a is not None:
            if isinstance(a, types.Real):
                a = a
            elif isinstance(a, int) or isinstance(a, float):
                a = types.Real(a)
            elif isinstance(a, str):
                a = types.Real.from_mcnp(a)

        if a is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, a)

        self._a: types.Real = a

    @property
    def b(self) -> types.Real:
        """
        Built-in function parameter #2

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._b

    @b.setter
    def b(self, b: str | int | float | types.Real) -> None:
        """
        Sets `b`.

        Parameters:
            b: Built-in function parameter #2.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if b is not None:
            if isinstance(b, types.Real):
                b = b
            elif isinstance(b, int) or isinstance(b, float):
                b = types.Real(b)
            elif isinstance(b, str):
                b = types.Real.from_mcnp(b)

        self._b: types.Real = b
