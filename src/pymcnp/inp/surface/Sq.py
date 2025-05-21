import re
import copy
import typing
import dataclasses


from ._option import SurfaceOption
from ...utils import types
from ...utils import errors


class Sq(SurfaceOption):
    """
    Represents INP sq elements.

    Attributes:
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
    """

    _KEYWORD = 'sq'

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

    _REGEX = re.compile(
        rf'\Asq( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})\Z'
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
        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x)
        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y)
        if z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z)

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


@dataclasses.dataclass
class SqBuilder:
    """
    Builds ``Sq``.

    Attributes:
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
    """

    a: str | float | types.Real
    b: str | float | types.Real
    c: str | float | types.Real
    d: str | float | types.Real
    e: str | float | types.Real
    f: str | float | types.Real
    g: str | float | types.Real
    x: str | float | types.Real
    y: str | float | types.Real
    z: str | float | types.Real

    def build(self):
        """
        Builds ``SqBuilder`` into ``Sq``.

        Returns:
            ``Sq`` for ``SqBuilder``.
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

        x = self.x
        if isinstance(self.x, types.Real):
            x = self.x
        elif isinstance(self.x, float) or isinstance(self.x, int):
            x = types.Real(self.x)
        elif isinstance(self.x, str):
            x = types.Real.from_mcnp(self.x)

        y = self.y
        if isinstance(self.y, types.Real):
            y = self.y
        elif isinstance(self.y, float) or isinstance(self.y, int):
            y = types.Real(self.y)
        elif isinstance(self.y, str):
            y = types.Real.from_mcnp(self.y)

        z = self.z
        if isinstance(self.z, types.Real):
            z = self.z
        elif isinstance(self.z, float) or isinstance(self.z, int):
            z = types.Real(self.z)
        elif isinstance(self.z, str):
            z = types.Real.from_mcnp(self.z)

        return Sq(
            a=a,
            b=b,
            c=c,
            d=d,
            e=e,
            f=f,
            g=g,
            x=x,
            y=y,
            z=z,
        )

    @staticmethod
    def unbuild(ast: Sq):
        """
        Unbuilds ``Sq`` into ``SqBuilder``

        Returns:
            ``SqBuilder`` for ``Sq``.
        """

        return Sq(
            a=copy.deepcopy(ast.a),
            b=copy.deepcopy(ast.b),
            c=copy.deepcopy(ast.c),
            d=copy.deepcopy(ast.d),
            e=copy.deepcopy(ast.e),
            f=copy.deepcopy(ast.f),
            g=copy.deepcopy(ast.g),
            x=copy.deepcopy(ast.x),
            y=copy.deepcopy(ast.y),
            z=copy.deepcopy(ast.z),
        )
