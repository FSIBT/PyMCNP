import re
import copy
import typing
import dataclasses


from ._option import SurfaceOption
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Rec(SurfaceOption):
    """
    Represents INP rec elements.

    Attributes:
        vx: Elliptical cylinder position vector x component.
        vy: Elliptical cylinder position vector y component.
        vz: Elliptical cylinder position vector z component.
        hx: Elliptical cylinder height vector x component.
        hy: Elliptical cylinder height vector y component.
        hz: Elliptical cylinder height vector z component.
        v1x: Elliptical cylinder major axis vector x component.
        v1y: Elliptical cylinder major axis vector y component.
        v1z: Elliptical cylinder major axis vector z component.
        v2x: Elliptical cylinder minor axis vector x component.
        v2y: Elliptical cylinder minor axis vector y component.
        v2z: Elliptical cylinder minor axis vector z component.
    """

    _KEYWORD = 'rec'

    _ATTRS = {
        'vx': types.Real,
        'vy': types.Real,
        'vz': types.Real,
        'hx': types.Real,
        'hy': types.Real,
        'hz': types.Real,
        'v1x': types.Real,
        'v1y': types.Real,
        'v1z': types.Real,
        'v2x': types.Real,
        'v2y': types.Real,
        'v2z': types.Real,
    }

    _REGEX = re.compile(
        rf'\Arec( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})?( {types.Real._REGEX.pattern})?\Z'
    )

    def __init__(
        self,
        vx: types.Real,
        vy: types.Real,
        vz: types.Real,
        hx: types.Real,
        hy: types.Real,
        hz: types.Real,
        v1x: types.Real,
        v1y: types.Real,
        v1z: types.Real,
        v2x: types.Real,
        v2y: types.Real = None,
        v2z: types.Real = None,
    ):
        """
        Initializes ``Rec``.

        Parameters:
            vx: Elliptical cylinder position vector x component.
            vy: Elliptical cylinder position vector y component.
            vz: Elliptical cylinder position vector z component.
            hx: Elliptical cylinder height vector x component.
            hy: Elliptical cylinder height vector y component.
            hz: Elliptical cylinder height vector z component.
            v1x: Elliptical cylinder major axis vector x component.
            v1y: Elliptical cylinder major axis vector y component.
            v1z: Elliptical cylinder major axis vector z component.
            v2x: Elliptical cylinder minor axis vector x component.
            v2y: Elliptical cylinder minor axis vector y component.
            v2z: Elliptical cylinder minor axis vector z component.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if vx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, vx)
        if vy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, vy)
        if vz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, vz)
        if hx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, hx)
        if hy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, hy)
        if hz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, hz)
        if v1x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v1x)
        if v1y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v1y)
        if v1z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v1z)
        if v2x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v2x)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                vx,
                vy,
                vz,
                hx,
                hy,
                hz,
                v1x,
                v1y,
                v1z,
                v2x,
                v2y,
                v2z,
            ]
        )

        self.vx: typing.Final[types.Real] = vx
        self.vy: typing.Final[types.Real] = vy
        self.vz: typing.Final[types.Real] = vz
        self.hx: typing.Final[types.Real] = hx
        self.hy: typing.Final[types.Real] = hy
        self.hz: typing.Final[types.Real] = hz
        self.v1x: typing.Final[types.Real] = v1x
        self.v1y: typing.Final[types.Real] = v1y
        self.v1z: typing.Final[types.Real] = v1z
        self.v2x: typing.Final[types.Real] = v2x
        self.v2y: typing.Final[types.Real] = v2y
        self.v2z: typing.Final[types.Real] = v2z

    def draw(self):
        """
        Generates ``Visualization`` from ``Rec``.

        Returns:
            ``pyvista.PolyData`` for ``Rec``
        """

        v = _visualization.Vector(self.vx.value, self.vy.value, self.vz.value)
        h = _visualization.Vector(self.hx.value, self.hy.value, self.hz.value)
        v1 = _visualization.Vector(self.v1x.value, self.v1y.value, self.v1z.value)
        v2 = _visualization.Vector(self.v2x.value, self.v2y.value, self.v2z.value)

        cross = v * _visualization.Vector(0, 0, 1)
        angle = v & _visualization.Vector(0, 0, 1)

        vis = _visualization.Visualization.get_cylinder_ellipse(h.norm(), v1.norm(), v2.norm())
        vis = vis.add_rotation(cross, angle, (0, 0, 0))
        vis = vis.add_translation(v)

        return vis


@dataclasses.dataclass
class RecBuilder:
    """
    Builds ``Rec``.

    Attributes:
        vx: Elliptical cylinder position vector x component.
        vy: Elliptical cylinder position vector y component.
        vz: Elliptical cylinder position vector z component.
        hx: Elliptical cylinder height vector x component.
        hy: Elliptical cylinder height vector y component.
        hz: Elliptical cylinder height vector z component.
        v1x: Elliptical cylinder major axis vector x component.
        v1y: Elliptical cylinder major axis vector y component.
        v1z: Elliptical cylinder major axis vector z component.
        v2x: Elliptical cylinder minor axis vector x component.
        v2y: Elliptical cylinder minor axis vector y component.
        v2z: Elliptical cylinder minor axis vector z component.
    """

    vx: str | float | types.Real
    vy: str | float | types.Real
    vz: str | float | types.Real
    hx: str | float | types.Real
    hy: str | float | types.Real
    hz: str | float | types.Real
    v1x: str | float | types.Real
    v1y: str | float | types.Real
    v1z: str | float | types.Real
    v2x: str | float | types.Real
    v2y: str | float | types.Real = None
    v2z: str | float | types.Real = None

    def build(self):
        """
        Builds ``RecBuilder`` into ``Rec``.

        Returns:
            ``Rec`` for ``RecBuilder``.
        """

        vx = self.vx
        if isinstance(self.vx, types.Real):
            vx = self.vx
        elif isinstance(self.vx, float) or isinstance(self.vx, int):
            vx = types.Real(self.vx)
        elif isinstance(self.vx, str):
            vx = types.Real.from_mcnp(self.vx)

        vy = self.vy
        if isinstance(self.vy, types.Real):
            vy = self.vy
        elif isinstance(self.vy, float) or isinstance(self.vy, int):
            vy = types.Real(self.vy)
        elif isinstance(self.vy, str):
            vy = types.Real.from_mcnp(self.vy)

        vz = self.vz
        if isinstance(self.vz, types.Real):
            vz = self.vz
        elif isinstance(self.vz, float) or isinstance(self.vz, int):
            vz = types.Real(self.vz)
        elif isinstance(self.vz, str):
            vz = types.Real.from_mcnp(self.vz)

        hx = self.hx
        if isinstance(self.hx, types.Real):
            hx = self.hx
        elif isinstance(self.hx, float) or isinstance(self.hx, int):
            hx = types.Real(self.hx)
        elif isinstance(self.hx, str):
            hx = types.Real.from_mcnp(self.hx)

        hy = self.hy
        if isinstance(self.hy, types.Real):
            hy = self.hy
        elif isinstance(self.hy, float) or isinstance(self.hy, int):
            hy = types.Real(self.hy)
        elif isinstance(self.hy, str):
            hy = types.Real.from_mcnp(self.hy)

        hz = self.hz
        if isinstance(self.hz, types.Real):
            hz = self.hz
        elif isinstance(self.hz, float) or isinstance(self.hz, int):
            hz = types.Real(self.hz)
        elif isinstance(self.hz, str):
            hz = types.Real.from_mcnp(self.hz)

        v1x = self.v1x
        if isinstance(self.v1x, types.Real):
            v1x = self.v1x
        elif isinstance(self.v1x, float) or isinstance(self.v1x, int):
            v1x = types.Real(self.v1x)
        elif isinstance(self.v1x, str):
            v1x = types.Real.from_mcnp(self.v1x)

        v1y = self.v1y
        if isinstance(self.v1y, types.Real):
            v1y = self.v1y
        elif isinstance(self.v1y, float) or isinstance(self.v1y, int):
            v1y = types.Real(self.v1y)
        elif isinstance(self.v1y, str):
            v1y = types.Real.from_mcnp(self.v1y)

        v1z = self.v1z
        if isinstance(self.v1z, types.Real):
            v1z = self.v1z
        elif isinstance(self.v1z, float) or isinstance(self.v1z, int):
            v1z = types.Real(self.v1z)
        elif isinstance(self.v1z, str):
            v1z = types.Real.from_mcnp(self.v1z)

        v2x = self.v2x
        if isinstance(self.v2x, types.Real):
            v2x = self.v2x
        elif isinstance(self.v2x, float) or isinstance(self.v2x, int):
            v2x = types.Real(self.v2x)
        elif isinstance(self.v2x, str):
            v2x = types.Real.from_mcnp(self.v2x)

        v2y = self.v2y
        if isinstance(self.v2y, types.Real):
            v2y = self.v2y
        elif isinstance(self.v2y, float) or isinstance(self.v2y, int):
            v2y = types.Real(self.v2y)
        elif isinstance(self.v2y, str):
            v2y = types.Real.from_mcnp(self.v2y)

        v2z = self.v2z
        if isinstance(self.v2z, types.Real):
            v2z = self.v2z
        elif isinstance(self.v2z, float) or isinstance(self.v2z, int):
            v2z = types.Real(self.v2z)
        elif isinstance(self.v2z, str):
            v2z = types.Real.from_mcnp(self.v2z)

        return Rec(
            vx=vx,
            vy=vy,
            vz=vz,
            hx=hx,
            hy=hy,
            hz=hz,
            v1x=v1x,
            v1y=v1y,
            v1z=v1z,
            v2x=v2x,
            v2y=v2y,
            v2z=v2z,
        )

    @staticmethod
    def unbuild(ast: Rec):
        """
        Unbuilds ``Rec`` into ``RecBuilder``

        Returns:
            ``RecBuilder`` for ``Rec``.
        """

        return Rec(
            vx=copy.deepcopy(ast.vx),
            vy=copy.deepcopy(ast.vy),
            vz=copy.deepcopy(ast.vz),
            hx=copy.deepcopy(ast.hx),
            hy=copy.deepcopy(ast.hy),
            hz=copy.deepcopy(ast.hz),
            v1x=copy.deepcopy(ast.v1x),
            v1y=copy.deepcopy(ast.v1y),
            v1z=copy.deepcopy(ast.v1z),
            v2x=copy.deepcopy(ast.v2x),
            v2y=copy.deepcopy(ast.v2y),
            v2z=copy.deepcopy(ast.v2z),
        )
