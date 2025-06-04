import re
import copy
import typing
import dataclasses


from ._option import SurfaceOption
from ...utils import types
from ...utils import errors


class Gq(SurfaceOption):
    """
    Represents INP gq elements.

    Attributes:
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
        rf'\Agq( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z'
    )

    def __init__(
        self,
        a: types.Real,
        b: types.Real,
        c: types.Real,
        d: types.Real,
        e: types.Real,
        f: types.Real,
        g: types.Real,
        h: types.Real,
        j: types.Real,
        k: types.Real,
    ):
        """
        Initializes ``Gq``.

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

        if a is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a)
        if b is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, b)
        if c is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, c)
        if d is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, d)
        if e is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, e)
        if f is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, f)
        if g is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, g)
        if h is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, h)
        if j is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, j)
        if k is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, k)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                a,
                b,
                c,
                d,
                e,
                f,
                g,
                h,
                j,
                k,
            ]
        )

        self.a: typing.Final[types.Real] = a
        self.b: typing.Final[types.Real] = b
        self.c: typing.Final[types.Real] = c
        self.d: typing.Final[types.Real] = d
        self.e: typing.Final[types.Real] = e
        self.f: typing.Final[types.Real] = f
        self.g: typing.Final[types.Real] = g
        self.h: typing.Final[types.Real] = h
        self.j: typing.Final[types.Real] = j
        self.k: typing.Final[types.Real] = k


@dataclasses.dataclass
class GqBuilder:
    """
    Builds ``Gq``.

    Attributes:
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
    """

    a: str | float | types.Real
    b: str | float | types.Real
    c: str | float | types.Real
    d: str | float | types.Real
    e: str | float | types.Real
    f: str | float | types.Real
    g: str | float | types.Real
    h: str | float | types.Real
    j: str | float | types.Real
    k: str | float | types.Real

    def build(self):
        """
        Builds ``GqBuilder`` into ``Gq``.

        Returns:
            ``Gq`` for ``GqBuilder``.
        """

        a = self.a
        if isinstance(self.a, types.Real):
            a = self.a
        elif isinstance(self.a, float) or isinstance(self.a, int):
            a = types.Real(self.a)
        elif isinstance(self.a, str):
            a = types.Real.from_mcnp(self.a)

        b = self.b
        if isinstance(self.b, types.Real):
            b = self.b
        elif isinstance(self.b, float) or isinstance(self.b, int):
            b = types.Real(self.b)
        elif isinstance(self.b, str):
            b = types.Real.from_mcnp(self.b)

        c = self.c
        if isinstance(self.c, types.Real):
            c = self.c
        elif isinstance(self.c, float) or isinstance(self.c, int):
            c = types.Real(self.c)
        elif isinstance(self.c, str):
            c = types.Real.from_mcnp(self.c)

        d = self.d
        if isinstance(self.d, types.Real):
            d = self.d
        elif isinstance(self.d, float) or isinstance(self.d, int):
            d = types.Real(self.d)
        elif isinstance(self.d, str):
            d = types.Real.from_mcnp(self.d)

        e = self.e
        if isinstance(self.e, types.Real):
            e = self.e
        elif isinstance(self.e, float) or isinstance(self.e, int):
            e = types.Real(self.e)
        elif isinstance(self.e, str):
            e = types.Real.from_mcnp(self.e)

        f = self.f
        if isinstance(self.f, types.Real):
            f = self.f
        elif isinstance(self.f, float) or isinstance(self.f, int):
            f = types.Real(self.f)
        elif isinstance(self.f, str):
            f = types.Real.from_mcnp(self.f)

        g = self.g
        if isinstance(self.g, types.Real):
            g = self.g
        elif isinstance(self.g, float) or isinstance(self.g, int):
            g = types.Real(self.g)
        elif isinstance(self.g, str):
            g = types.Real.from_mcnp(self.g)

        h = self.h
        if isinstance(self.h, types.Real):
            h = self.h
        elif isinstance(self.h, float) or isinstance(self.h, int):
            h = types.Real(self.h)
        elif isinstance(self.h, str):
            h = types.Real.from_mcnp(self.h)

        j = self.j
        if isinstance(self.j, types.Real):
            j = self.j
        elif isinstance(self.j, float) or isinstance(self.j, int):
            j = types.Real(self.j)
        elif isinstance(self.j, str):
            j = types.Real.from_mcnp(self.j)

        k = self.k
        if isinstance(self.k, types.Real):
            k = self.k
        elif isinstance(self.k, float) or isinstance(self.k, int):
            k = types.Real(self.k)
        elif isinstance(self.k, str):
            k = types.Real.from_mcnp(self.k)

        return Gq(
            a=a,
            b=b,
            c=c,
            d=d,
            e=e,
            f=f,
            g=g,
            h=h,
            j=j,
            k=k,
        )

    @staticmethod
    def unbuild(ast: Gq):
        """
        Unbuilds ``Gq`` into ``GqBuilder``

        Returns:
            ``GqBuilder`` for ``Gq``.
        """

        return Gq(
            a=copy.deepcopy(ast.a),
            b=copy.deepcopy(ast.b),
            c=copy.deepcopy(ast.c),
            d=copy.deepcopy(ast.d),
            e=copy.deepcopy(ast.e),
            f=copy.deepcopy(ast.f),
            g=copy.deepcopy(ast.g),
            h=copy.deepcopy(ast.h),
            j=copy.deepcopy(ast.j),
            k=copy.deepcopy(ast.k),
        )
