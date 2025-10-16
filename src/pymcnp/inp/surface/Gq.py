import re

from . import _option
from ... import types
from ... import errors


class Gq(_option.SurfaceOption):
    """
    Represents INP `gq` elements.
    """

    _KEYWORD = 'gq'

    _ATTRS = {
        'a': types.Real,
        'b': types.Real,
        'c': types.Real,
        'd': types.Real,
        'e': types.Real,
        'f': types.Real,
        'g': types.Real,
        'h': types.Real,
        'j': types.Real,
        'k': types.Real,
    }

    _REGEX = re.compile(
        rf'\Agq( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        a: str | int | float | types.Real,
        b: str | int | float | types.Real,
        c: str | int | float | types.Real,
        d: str | int | float | types.Real,
        e: str | int | float | types.Real,
        f: str | int | float | types.Real,
        g: str | int | float | types.Real,
        h: str | int | float | types.Real,
        j: str | int | float | types.Real,
        k: str | int | float | types.Real,
    ):
        """
        Initializes `Gq`.

        Parameters:
            a: Oblique special quadratic A coefficent.
            b: Oblique special quadratic B coefficent.
            c: Oblique special quadratic C coefficent.
            d: Oblique special quadratic D coefficent.
            e: Oblique special quadratic E coefficent.
            f: Oblique special quadratic F coefficent.
            g: Oblique special quadratic G coefficent.
            h: Oblique special quadratic H coefficent.
            j: Oblique special quadratic J coefficent.
            k: Oblique special quadratic K coefficent.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.a: types.Real = a
        self.b: types.Real = b
        self.c: types.Real = c
        self.d: types.Real = d
        self.e: types.Real = e
        self.f: types.Real = f
        self.g: types.Real = g
        self.h: types.Real = h
        self.j: types.Real = j
        self.k: types.Real = k

    @property
    def a(self) -> types.Real:
        """
        Oblique special quadratic A coefficent

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
            a: Oblique special quadratic A coefficent.

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
        Oblique special quadratic B coefficent

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
            b: Oblique special quadratic B coefficent.

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
        Oblique special quadratic C coefficent

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
            c: Oblique special quadratic C coefficent.

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
        Oblique special quadratic D coefficent

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
            d: Oblique special quadratic D coefficent.

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

    @property
    def e(self) -> types.Real:
        """
        Oblique special quadratic E coefficent

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._e

    @e.setter
    def e(self, e: str | int | float | types.Real) -> None:
        """
        Sets `e`.

        Parameters:
            e: Oblique special quadratic E coefficent.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if e is not None:
            if isinstance(e, types.Real):
                e = e
            elif isinstance(e, int) or isinstance(e, float):
                e = types.Real(e)
            elif isinstance(e, str):
                e = types.Real.from_mcnp(e)

        if e is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, e)

        self._e: types.Real = e

    @property
    def f(self) -> types.Real:
        """
        Oblique special quadratic F coefficent

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
            f: Oblique special quadratic F coefficent.

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
    def g(self) -> types.Real:
        """
        Oblique special quadratic G coefficent

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._g

    @g.setter
    def g(self, g: str | int | float | types.Real) -> None:
        """
        Sets `g`.

        Parameters:
            g: Oblique special quadratic G coefficent.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if g is not None:
            if isinstance(g, types.Real):
                g = g
            elif isinstance(g, int) or isinstance(g, float):
                g = types.Real(g)
            elif isinstance(g, str):
                g = types.Real.from_mcnp(g)

        if g is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, g)

        self._g: types.Real = g

    @property
    def h(self) -> types.Real:
        """
        Oblique special quadratic H coefficent

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._h

    @h.setter
    def h(self, h: str | int | float | types.Real) -> None:
        """
        Sets `h`.

        Parameters:
            h: Oblique special quadratic H coefficent.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if h is not None:
            if isinstance(h, types.Real):
                h = h
            elif isinstance(h, int) or isinstance(h, float):
                h = types.Real(h)
            elif isinstance(h, str):
                h = types.Real.from_mcnp(h)

        if h is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, h)

        self._h: types.Real = h

    @property
    def j(self) -> types.Real:
        """
        Oblique special quadratic J coefficent

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._j

    @j.setter
    def j(self, j: str | int | float | types.Real) -> None:
        """
        Sets `j`.

        Parameters:
            j: Oblique special quadratic J coefficent.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if j is not None:
            if isinstance(j, types.Real):
                j = j
            elif isinstance(j, int) or isinstance(j, float):
                j = types.Real(j)
            elif isinstance(j, str):
                j = types.Real.from_mcnp(j)

        if j is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, j)

        self._j: types.Real = j

    @property
    def k(self) -> types.Real:
        """
        Oblique special quadratic K coefficent

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._k

    @k.setter
    def k(self, k: str | int | float | types.Real) -> None:
        """
        Sets `k`.

        Parameters:
            k: Oblique special quadratic K coefficent.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if k is not None:
            if isinstance(k, types.Real):
                k = k
            elif isinstance(k, int) or isinstance(k, float):
                k = types.Real(k)
            elif isinstance(k, str):
                k = types.Real.from_mcnp(k)

        if k is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, k)

        self._k: types.Real = k
