import re

from . import _option
from ... import types
from ... import errors


class Factor(_option.MplotOption):
    """
    Represents INP `factor` elements.
    """

    _KEYWORD = 'factor'

    _ATTRS = {
        'a': types.String,
        'f': types.Real,
        's': types.Real,
    }

    _REGEX = re.compile(rf'\Afactor( {types.String._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)

    def __init__(self, a: str | types.String, f: str | int | float | types.Real, s: str | int | float | types.Real = None):
        """
        Initializes `Factor`.

        Parameters:
            a: Multiplication axis.
            f: Multiplication factor.
            s: Addative term.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.a: types.String = a
        self.f: types.Real = f
        self.s: types.Real = s

    @property
    def a(self) -> types.String:
        """
        Multiplication axis

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._a

    @a.setter
    def a(self, a: str | types.String) -> None:
        """
        Sets `a`.

        Parameters:
            a: Multiplication axis.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if a is not None:
            if isinstance(a, types.String):
                a = a
            elif isinstance(a, str):
                a = types.String.from_mcnp(a)

        if a is None or a.value.lower() not in {'x', 'y', 'z'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a)

        self._a: types.String = a

    @property
    def f(self) -> types.Real:
        """
        Multiplication factor

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._f

    @f.setter
    def f(self, f: str | int | float | types.Real) -> None:
        """
        Sets `f`.

        Parameters:
            f: Multiplication factor.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if f is not None:
            if isinstance(f, types.Real):
                f = f
            elif isinstance(f, int) or isinstance(f, float):
                f = types.Real(f)
            elif isinstance(f, str):
                f = types.Real.from_mcnp(f)

        if f is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, f)

        self._f: types.Real = f

    @property
    def s(self) -> types.Real:
        """
        Addative term

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._s

    @s.setter
    def s(self, s: str | int | float | types.Real) -> None:
        """
        Sets `s`.

        Parameters:
            s: Addative term.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if s is not None:
            if isinstance(s, types.Real):
                s = s
            elif isinstance(s, int) or isinstance(s, float):
                s = types.Real(s)
            elif isinstance(s, str):
                s = types.Real.from_mcnp(s)

        self._s: types.Real = s
