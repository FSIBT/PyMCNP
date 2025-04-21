import re
import typing
import dataclasses


from ._option import SurfaceOption
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Box(SurfaceOption, keyword='box'):
    """
    Represents INP box elements.

    Attributes:
        vx: Box macrobody position vector x component.
        vy: Box macrobody position vector y component.
        vz: Box macrobody position vector z component.
        a1x: Box macrobody vector #1 x component.
        a1y: Box macrobody vector #1 y component.
        a1z: Box macrobody vector #1 z component.
        a2x: Box macrobody vector #2 x component.
        a2y: Box macrobody vector #2 y component.
        a2z: Box macrobody vector #2 z component.
        a3x: Box macrobody vector #3 x component.
        a3y: Box macrobody vector #3 y component.
        a3z: Box macrobody vector #3 z component.
    """

    _ATTRS = {
        'vx': types.Real,
        'vy': types.Real,
        'vz': types.Real,
        'a1x': types.Real,
        'a1y': types.Real,
        'a1z': types.Real,
        'a2x': types.Real,
        'a2y': types.Real,
        'a2z': types.Real,
        'a3x': types.Real,
        'a3y': types.Real,
        'a3z': types.Real,
    }

    _REGEX = re.compile(
        rf'\Abox( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        vx: types.Real,
        vy: types.Real,
        vz: types.Real,
        a1x: types.Real,
        a1y: types.Real,
        a1z: types.Real,
        a2x: types.Real,
        a2y: types.Real,
        a2z: types.Real,
        a3x: types.Real,
        a3y: types.Real,
        a3z: types.Real,
    ):
        """
        Initializes ``Box``.

        Parameters:
            vx: Box macrobody position vector x component.
            vy: Box macrobody position vector y component.
            vz: Box macrobody position vector z component.
            a1x: Box macrobody vector #1 x component.
            a1y: Box macrobody vector #1 y component.
            a1z: Box macrobody vector #1 z component.
            a2x: Box macrobody vector #2 x component.
            a2y: Box macrobody vector #2 y component.
            a2z: Box macrobody vector #2 z component.
            a3x: Box macrobody vector #3 x component.
            a3y: Box macrobody vector #3 y component.
            a3z: Box macrobody vector #3 z component.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if vx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, vx)
        if vy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, vy)
        if vz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, vz)
        if a1x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a1x)
        if a1y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a1y)
        if a1z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a1z)
        if a2x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a2x)
        if a2y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a2y)
        if a2z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a2z)
        if a3x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a3x)
        if a3y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a3y)
        if a3z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a3z)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                vx,
                vy,
                vz,
                a1x,
                a1y,
                a1z,
                a2x,
                a2y,
                a2z,
                a3x,
                a3y,
                a3z,
            ]
        )

        self.vx: typing.Final[types.Real] = vx
        self.vy: typing.Final[types.Real] = vy
        self.vz: typing.Final[types.Real] = vz
        self.a1x: typing.Final[types.Real] = a1x
        self.a1y: typing.Final[types.Real] = a1y
        self.a1z: typing.Final[types.Real] = a1z
        self.a2x: typing.Final[types.Real] = a2x
        self.a2y: typing.Final[types.Real] = a2y
        self.a2z: typing.Final[types.Real] = a2z
        self.a3x: typing.Final[types.Real] = a3x
        self.a3y: typing.Final[types.Real] = a3y
        self.a3z: typing.Final[types.Real] = a3z

    def draw(self):
        """
        Generates ``Visualization`` from ``Box``.

        Returns:
            ``pyvista.PolyData`` for ``Box``.
        """

        v = _visualization.Vector(self.vx.value, self.vy.value, self.vz.value)
        a1 = _visualization.Vector(self.a1x.value, self.a1y.value, self.a1z.value)
        a2 = _visualization.Vector(self.a2x.value, self.a2y.value, self.a2z.value)
        a3 = _visualization.Vector(self.a3x.value, self.a3y.value, self.a3z.value)
        cross = _visualization.Vector(1, 0, 0) * a1
        angle = _visualization.Vector(1, 0, 0) & a1

        vis = _visualization.Visualization.get_box(a1.norm(), a2.norm(), a3.norm())
        vis = vis.add_rotation(cross, angle, (0, 0, 0))
        vis = vis.add_translation(v)

        return vis


@dataclasses.dataclass
class BoxBuilder:
    """
    Builds ``Box``.

    Attributes:
        vx: Box macrobody position vector x component.
        vy: Box macrobody position vector y component.
        vz: Box macrobody position vector z component.
        a1x: Box macrobody vector #1 x component.
        a1y: Box macrobody vector #1 y component.
        a1z: Box macrobody vector #1 z component.
        a2x: Box macrobody vector #2 x component.
        a2y: Box macrobody vector #2 y component.
        a2z: Box macrobody vector #2 z component.
        a3x: Box macrobody vector #3 x component.
        a3y: Box macrobody vector #3 y component.
        a3z: Box macrobody vector #3 z component.
    """

    vx: str | float | types.Real
    vy: str | float | types.Real
    vz: str | float | types.Real
    a1x: str | float | types.Real
    a1y: str | float | types.Real
    a1z: str | float | types.Real
    a2x: str | float | types.Real
    a2y: str | float | types.Real
    a2z: str | float | types.Real
    a3x: str | float | types.Real
    a3y: str | float | types.Real
    a3z: str | float | types.Real

    def build(self):
        """
        Builds ``BoxBuilder`` into ``Box``.

        Returns:
            ``Box`` for ``BoxBuilder``.
        """

        if isinstance(self.vx, types.Real):
            vx = self.vx
        elif isinstance(self.vx, float) or isinstance(self.vx, int):
            vx = types.Real(self.vx)
        elif isinstance(self.vx, str):
            vx = types.Real.from_mcnp(self.vx)

        if isinstance(self.vy, types.Real):
            vy = self.vy
        elif isinstance(self.vy, float) or isinstance(self.vy, int):
            vy = types.Real(self.vy)
        elif isinstance(self.vy, str):
            vy = types.Real.from_mcnp(self.vy)

        if isinstance(self.vz, types.Real):
            vz = self.vz
        elif isinstance(self.vz, float) or isinstance(self.vz, int):
            vz = types.Real(self.vz)
        elif isinstance(self.vz, str):
            vz = types.Real.from_mcnp(self.vz)

        if isinstance(self.a1x, types.Real):
            a1x = self.a1x
        elif isinstance(self.a1x, float) or isinstance(self.a1x, int):
            a1x = types.Real(self.a1x)
        elif isinstance(self.a1x, str):
            a1x = types.Real.from_mcnp(self.a1x)

        if isinstance(self.a1y, types.Real):
            a1y = self.a1y
        elif isinstance(self.a1y, float) or isinstance(self.a1y, int):
            a1y = types.Real(self.a1y)
        elif isinstance(self.a1y, str):
            a1y = types.Real.from_mcnp(self.a1y)

        if isinstance(self.a1z, types.Real):
            a1z = self.a1z
        elif isinstance(self.a1z, float) or isinstance(self.a1z, int):
            a1z = types.Real(self.a1z)
        elif isinstance(self.a1z, str):
            a1z = types.Real.from_mcnp(self.a1z)

        if isinstance(self.a2x, types.Real):
            a2x = self.a2x
        elif isinstance(self.a2x, float) or isinstance(self.a2x, int):
            a2x = types.Real(self.a2x)
        elif isinstance(self.a2x, str):
            a2x = types.Real.from_mcnp(self.a2x)

        if isinstance(self.a2y, types.Real):
            a2y = self.a2y
        elif isinstance(self.a2y, float) or isinstance(self.a2y, int):
            a2y = types.Real(self.a2y)
        elif isinstance(self.a2y, str):
            a2y = types.Real.from_mcnp(self.a2y)

        if isinstance(self.a2z, types.Real):
            a2z = self.a2z
        elif isinstance(self.a2z, float) or isinstance(self.a2z, int):
            a2z = types.Real(self.a2z)
        elif isinstance(self.a2z, str):
            a2z = types.Real.from_mcnp(self.a2z)

        if isinstance(self.a3x, types.Real):
            a3x = self.a3x
        elif isinstance(self.a3x, float) or isinstance(self.a3x, int):
            a3x = types.Real(self.a3x)
        elif isinstance(self.a3x, str):
            a3x = types.Real.from_mcnp(self.a3x)

        if isinstance(self.a3y, types.Real):
            a3y = self.a3y
        elif isinstance(self.a3y, float) or isinstance(self.a3y, int):
            a3y = types.Real(self.a3y)
        elif isinstance(self.a3y, str):
            a3y = types.Real.from_mcnp(self.a3y)

        if isinstance(self.a3z, types.Real):
            a3z = self.a3z
        elif isinstance(self.a3z, float) or isinstance(self.a3z, int):
            a3z = types.Real(self.a3z)
        elif isinstance(self.a3z, str):
            a3z = types.Real.from_mcnp(self.a3z)

        return Box(
            vx=vx,
            vy=vy,
            vz=vz,
            a1x=a1x,
            a1y=a1y,
            a1z=a1z,
            a2x=a2x,
            a2y=a2y,
            a2z=a2z,
            a3x=a3x,
            a3y=a3y,
            a3z=a3z,
        )
