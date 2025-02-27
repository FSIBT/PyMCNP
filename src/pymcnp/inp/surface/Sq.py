import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors


class Sq(SurfaceOption_, keyword='sq'):
    """
    Represents INP sq elements.

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
        'x': types.Real,
        'y': types.Real,
        'z': types.Real,
    }

    _REGEX = re.compile(r'sq( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)')

    def __init__(
        self,
        a: types.Real,
        b: types.Real,
        c: types.Real,
        d: types.Real,
        e: types.Real,
        f: types.Real,
        g: types.Real,
        x: types.Real,
        y: types.Real,
        z: types.Real,
    ):
        """
        Initializes ``Sq``.

        Parameters:
            a: Oblique special quadratic A coefficent.
            b: Oblique special quadratic B coefficent.
            c: Oblique special quadratic C coefficent.
            d: Oblique special quadratic D coefficent.
            e: Oblique special quadratic E coefficent.
            f: Oblique special quadratic F coefficent.
            g: Oblique special quadratic G coefficent.
            x: Oblique special quadratic center x component.
            y: Oblique special quadratic center y component.
            z: Oblique special quadratic center z component.

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
        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x)
        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, y)
        if z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, z)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                a,
                b,
                c,
                d,
                e,
                f,
                g,
                x,
                y,
                z,
            ]
        )

        self.a: typing.Final[types.Real] = a
        self.b: typing.Final[types.Real] = b
        self.c: typing.Final[types.Real] = c
        self.d: typing.Final[types.Real] = d
        self.e: typing.Final[types.Real] = e
        self.f: typing.Final[types.Real] = f
        self.g: typing.Final[types.Real] = g
        self.x: typing.Final[types.Real] = x
        self.y: typing.Final[types.Real] = y
        self.z: typing.Final[types.Real] = z
