import re

from . import _option
from ... import _show
from ... import types
from ... import errors


class P_0(_option.SurfaceOption):
    """
    Represents INP `p` elements variation #0.
    """

    _KEYWORD = 'p'

    _ATTRS = {
        'a': types.Real,
        'b': types.Real,
        'c': types.Real,
        'd': types.Real,
    }

    _REGEX = re.compile(rf'\Ap( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, a: str | int | float | types.Real, b: str | int | float | types.Real, c: str | int | float | types.Real, d: str | int | float | types.Real):
        """
        Initializes `P_0`.

        Parameters:
            a: Equation-defined general plane A coefficent.
            b: Equation-defined general plane B coefficent.
            c: Equation-defined general plane C coefficent.
            d: Equation-defined general plane D coefficent.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.a: types.Real = a
        self.b: types.Real = b
        self.c: types.Real = c
        self.d: types.Real = d

    @property
    def a(self) -> types.Real:
        """
        Equation-defined general plane A coefficent

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._a

    @a.setter
    def a(self, a: str | int | float | types.Real) -> None:
        """
        Sets `a`.

        Parameters:
            a: Equation-defined general plane A coefficent.

        Raises:
            InpError: SEMANTICS_OPTION.
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
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a)

        self._a: types.Real = a

    @property
    def b(self) -> types.Real:
        """
        Equation-defined general plane B coefficent

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._b

    @b.setter
    def b(self, b: str | int | float | types.Real) -> None:
        """
        Sets `b`.

        Parameters:
            b: Equation-defined general plane B coefficent.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if b is not None:
            if isinstance(b, types.Real):
                b = b
            elif isinstance(b, int) or isinstance(b, float):
                b = types.Real(b)
            elif isinstance(b, str):
                b = types.Real.from_mcnp(b)

        if b is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, b)

        self._b: types.Real = b

    @property
    def c(self) -> types.Real:
        """
        Equation-defined general plane C coefficent

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._c

    @c.setter
    def c(self, c: str | int | float | types.Real) -> None:
        """
        Sets `c`.

        Parameters:
            c: Equation-defined general plane C coefficent.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if c is not None:
            if isinstance(c, types.Real):
                c = c
            elif isinstance(c, int) or isinstance(c, float):
                c = types.Real(c)
            elif isinstance(c, str):
                c = types.Real.from_mcnp(c)

        if c is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, c)

        self._c: types.Real = c

    @property
    def d(self) -> types.Real:
        """
        Equation-defined general plane D coefficent

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._d

    @d.setter
    def d(self, d: str | int | float | types.Real) -> None:
        """
        Sets `d`.

        Parameters:
            d: Equation-defined general plane D coefficent.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if d is not None:
            if isinstance(d, types.Real):
                d = d
            elif isinstance(d, int) or isinstance(d, float):
                d = types.Real(d)
            elif isinstance(d, str):
                d = types.Real.from_mcnp(d)

        if d is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, d)

        self._d: types.Real = d

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Px`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Px`
        """

        vis = shapes.Plane(float(self.a), float(self.b), float(self.c), float(self.d))

        return vis
