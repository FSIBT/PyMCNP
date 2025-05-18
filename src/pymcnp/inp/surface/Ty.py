import re
import typing
import dataclasses


from ._option import SurfaceOption
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Ty(SurfaceOption):
    """
    Represents INP ty elements.

    Attributes:
        x: Parallel-to-y-axis tori center x component.
        y: Parallel-to-y-axis tori center y component.
        z: Parallel-to-y-axis tori center z component.
        a: Parallel-to-y-axis tori A coefficent.
        b: Parallel-to-y-axis tori B coefficent.
        c: Parallel-to-y-axis tori C coefficent.
    """

    _ATTRS = {
        'x': types.Real,
        'y': types.Real,
        'z': types.Real,
        'a': types.Real,
        'b': types.Real,
        'c': types.Real,
    }

    _REGEX = re.compile(
        rf'\Aty( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        x: types.Real,
        y: types.Real,
        z: types.Real,
        a: types.Real,
        b: types.Real,
        c: types.Real,
    ):
        """
        Initializes ``Ty``.

        Parameters:
            x: Parallel-to-y-axis tori center x component.
            y: Parallel-to-y-axis tori center y component.
            z: Parallel-to-y-axis tori center z component.
            a: Parallel-to-y-axis tori A coefficent.
            b: Parallel-to-y-axis tori B coefficent.
            c: Parallel-to-y-axis tori C coefficent.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x)
        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y)
        if z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z)
        if a is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a)
        if b is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, b)
        if c is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, c)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x,
                y,
                z,
                a,
                b,
                c,
            ]
        )

        self.x: typing.Final[types.Real] = x
        self.y: typing.Final[types.Real] = y
        self.z: typing.Final[types.Real] = z
        self.a: typing.Final[types.Real] = a
        self.b: typing.Final[types.Real] = b
        self.c: typing.Final[types.Real] = c

    def draw(self):
        """
        Generates ``Visualization`` from ``Ty``.

        Returns:
            ``pyvista.PolyData`` for ``Ty``
        """

        vis = _visualization.Visualization.get_torus(self.b.value, self.c.value, self.a.value)
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x.value, self.y.value, self.z.value))

        return vis


@dataclasses.dataclass
class TyBuilder:
    """
    Builds ``Ty``.

    Attributes:
        x: Parallel-to-y-axis tori center x component.
        y: Parallel-to-y-axis tori center y component.
        z: Parallel-to-y-axis tori center z component.
        a: Parallel-to-y-axis tori A coefficent.
        b: Parallel-to-y-axis tori B coefficent.
        c: Parallel-to-y-axis tori C coefficent.
    """

    x: str | float | types.Real
    y: str | float | types.Real
    z: str | float | types.Real
    a: str | float | types.Real
    b: str | float | types.Real
    c: str | float | types.Real

    def build(self):
        """
        Builds ``TyBuilder`` into ``Ty``.

        Returns:
            ``Ty`` for ``TyBuilder``.
        """

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

        return Ty(
            x=x,
            y=y,
            z=z,
            a=a,
            b=b,
            c=c,
        )
