import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors


class Gq(SurfaceOption_, keyword='gq'):
    """
    Represents INP gq elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

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
        rf'gq( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
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
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if a is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, a)
        if b is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, b)
        if c is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, c)
        if d is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, d)
        if e is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, e)
        if f is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, f)
        if g is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, g)
        if h is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, h)
        if j is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, j)
        if k is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, k)

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
