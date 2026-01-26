import re

from . import _card
from .. import types
from .. import errors


class Gq(_card.Card):
    """
    Represents INP `gq` surface cards.
    """

    _KEYWORD = 'gq'

    _ATTRS = {
        'prefix': types.String,
        'number': types.Integer,
        'transform': types.Integer,
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
        rf'\A(\+|\*)?(\S+)( \S+)? gq( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
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
        number: types.Integer = None,
        transform: types.Integer = None,
        prefix: str = None,
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
            number: surface number.
            transform: surface transformation.
            prefix: surface whitebody flag.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        if number is None:
            number = next(_card.NUMBER)

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
        self.transform: types.Integer = transform
        self.number: types.Integer = number
        self.prefix: types.String = prefix

    @property
    def a(self) -> types.Real:
        """
        Oblique special quadratic A coefficent

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
            a: Oblique special quadratic A coefficent.

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
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a)

        self._a: types.Real = a

    @property
    def b(self) -> types.Real:
        """
        Oblique special quadratic B coefficent

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
            b: Oblique special quadratic B coefficent.

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

        if b is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, b)

        self._b: types.Real = b

    @property
    def c(self) -> types.Real:
        """
        Oblique special quadratic C coefficent

        Raises:
            InpError: SEMANTICS_CARD.
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
            InpError: SEMANTICS_CARD.
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
            InpError: SEMANTICS_CARD.
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
            InpError: SEMANTICS_CARD.
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
            InpError: SEMANTICS_CARD.
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
            InpError: SEMANTICS_CARD.
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
            InpError: SEMANTICS_CARD.
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
            InpError: SEMANTICS_CARD.
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
            InpError: SEMANTICS_CARD.
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
            InpError: SEMANTICS_CARD.
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
            InpError: SEMANTICS_CARD.
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
            InpError: SEMANTICS_CARD.
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
            InpError: SEMANTICS_CARD.
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
            InpError: SEMANTICS_CARD.
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
            InpError: SEMANTICS_CARD.
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
            InpError: SEMANTICS_CARD.
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

    def __and__(a, b):
        """
        Unites `Surface`.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            `Surface` union.
        """

        return types.Geometry.from_mcnp(f'{a.number}:{b.number}')

    def __or__(a, b):
        """
        Intersects `Surface`.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            `Surface` intersection.
        """

        return types.Geometry.from_mcnp(f'{a.number} {b.number}')

    def __neg__(self):
        """
        Negatives `Surface`.

        Returns:
            `Surface` negative.
        """

        return types.Geometry.from_mcnp(f'-{self.number}')

    def __pos__(self):
        """
        Positives `Surface`.

        Returns:
            `Surface` positive.
        """

        return types.Geometry.from_mcnp(f'+{self.number}')

    def __invert__(self):
        """
        Inverts `Surface`.

        Returns:
            `Surface` complement.
        """

        return types.Geometry.from_mcnp(f'#{self.number}')

    @property
    def number(self) -> types.Integer:
        """
        Surface number.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._number

    @number.setter
    def number(self, number: str | int | types.Integer) -> None:
        """
        Sets `number`.

        Parameters:
            number: Surface number.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if number is not None:
            if isinstance(number, types.Integer):
                number = number
            elif isinstance(number, int):
                number = types.Integer(number)
            elif isinstance(number, str):
                number = types.Integer.from_mcnp(number)

        if number is None or not (1 <= number <= (99_999_999 if not self.transform else 999)):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, number)

        self._number: types.Integer = number

    @property
    def transform(self) -> types.Integer:
        """
        Surface transform.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._transform

    @transform.setter
    def transform(self, transform: str | int | types.Integer = None) -> None:
        """
        Sets `transform`.

        Parameters:
            transform: Surface transform.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if transform is not None:
            if isinstance(transform, types.Integer):
                transform = transform
            elif isinstance(transform, int):
                transform = types.Integer(transform)
            elif isinstance(transform, str):
                transform = types.Integer.from_mcnp(transform)

        if transform is not None and not (0 <= transform <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, transform)

        self._transform: types.Integer = transform

    @property
    def prefix(self) -> types.String:
        """
        Surface whitebody/reflecting flag.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._prefix

    @prefix.setter
    def prefix(self, prefix: str | types.String) -> None:
        """
        Sets `prefix`.

        Parameters:
            prefix: Surface whitebody/reflecting flag.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if prefix is not None:
            if isinstance(prefix, types.String):
                prefix = prefix
            elif isinstance(prefix, str):
                prefix = types.String.from_mcnp(prefix)

        if prefix is not None and prefix.value.lower() not in {'*', '+'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, prefix)

        self._prefix: types.String = prefix

    def to_mcnp(self):
        """
        Generates INP from `Gq`.

        Returns:
            INP surface card.
        """

        source = f'{self.prefix if self.prefix is not None else ""}{self.number} {self.transform if self.transform is not None else ""} {self._KEYWORD} {self.a} {self.b} {self.c} {self.d} {self.e} {self.f} {self.g} {self.h} {self.j} {self.k}'
        source = _card.Card._postprocess(source)

        return source
