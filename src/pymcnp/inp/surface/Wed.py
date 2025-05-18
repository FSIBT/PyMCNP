import re
import typing
import dataclasses


from ._option import SurfaceOption
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Wed(SurfaceOption):
    """
    Represents INP wed elements.

    Attributes:
        vx: Wedge position vector x component.
        vy: Wedge position vector y component.
        vz: Wedge position vector z component.
        v1x: Wedge side vector #1 x component.
        v1y: Wedge side vector #1 y component.
        v1z: Wedge side vector #1 z component.
        v2x: Wedge side vector #2 x component.
        v2y: Wedge side vector #2 y component.
        v2z: Wedge side vector #2 z component.
        v3x: Wedge height vector x component.
        v3y: Wedge height vector y component.
        v3z: Wedge height vector z component.
    """

    _ATTRS = {
        'vx': types.Real,
        'vy': types.Real,
        'vz': types.Real,
        'v1x': types.Real,
        'v1y': types.Real,
        'v1z': types.Real,
        'v2x': types.Real,
        'v2y': types.Real,
        'v2z': types.Real,
        'v3x': types.Real,
        'v3y': types.Real,
        'v3z': types.Real,
    }

    _REGEX = re.compile(
        rf'\Awed( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        vx: types.Real,
        vy: types.Real,
        vz: types.Real,
        v1x: types.Real,
        v1y: types.Real,
        v1z: types.Real,
        v2x: types.Real,
        v2y: types.Real,
        v2z: types.Real,
        v3x: types.Real,
        v3y: types.Real,
        v3z: types.Real,
    ):
        """
        Initializes ``Wed``.

        Parameters:
            vx: Wedge position vector x component.
            vy: Wedge position vector y component.
            vz: Wedge position vector z component.
            v1x: Wedge side vector #1 x component.
            v1y: Wedge side vector #1 y component.
            v1z: Wedge side vector #1 z component.
            v2x: Wedge side vector #2 x component.
            v2y: Wedge side vector #2 y component.
            v2z: Wedge side vector #2 z component.
            v3x: Wedge height vector x component.
            v3y: Wedge height vector y component.
            v3z: Wedge height vector z component.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if vx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, vx)
        if vy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, vy)
        if vz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, vz)
        if v1x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v1x)
        if v1y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v1y)
        if v1z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v1z)
        if v2x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v2x)
        if v2y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v2y)
        if v2z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v2z)
        if v3x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v3x)
        if v3y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v3y)
        if v3z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v3z)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                vx,
                vy,
                vz,
                v1x,
                v1y,
                v1z,
                v2x,
                v2y,
                v2z,
                v3x,
                v3y,
                v3z,
            ]
        )

        self.vx: typing.Final[types.Real] = vx
        self.vy: typing.Final[types.Real] = vy
        self.vz: typing.Final[types.Real] = vz
        self.v1x: typing.Final[types.Real] = v1x
        self.v1y: typing.Final[types.Real] = v1y
        self.v1z: typing.Final[types.Real] = v1z
        self.v2x: typing.Final[types.Real] = v2x
        self.v2y: typing.Final[types.Real] = v2y
        self.v2z: typing.Final[types.Real] = v2z
        self.v3x: typing.Final[types.Real] = v3x
        self.v3y: typing.Final[types.Real] = v3y
        self.v3z: typing.Final[types.Real] = v3z

    def draw(self):
        """
        Generates ``Visualization`` from ``Wed``.

        Returns:
            ``pyvista.PolyData`` for ``Wed``
        """

        v = _visualization.Vector(self.vx.value, self.vy.value, self.vz.value)
        v1 = _visualization.Vector(self.v1x.value, self.v1y.value, self.v1z.value)
        v2 = _visualization.Vector(self.v2x.value, self.v2y.value, self.v2z.value)
        v3 = _visualization.Vector(self.v3x.value, self.v3y.value, self.v3z.value)

        cross = _visualization.Vector(1, 0, 0) * v1
        angle = _visualization.Vector(1, 0, 0) & v1

        vis = _visualization.Visualization.get_wedge(v1.norm(), v2.norm(), v3.norm())
        vis = vis.add_rotation(cross, angle, (0, 0, 0))
        vis = vis.add_translation(v)

        return vis


@dataclasses.dataclass
class WedBuilder:
    """
    Builds ``Wed``.

    Attributes:
        vx: Wedge position vector x component.
        vy: Wedge position vector y component.
        vz: Wedge position vector z component.
        v1x: Wedge side vector #1 x component.
        v1y: Wedge side vector #1 y component.
        v1z: Wedge side vector #1 z component.
        v2x: Wedge side vector #2 x component.
        v2y: Wedge side vector #2 y component.
        v2z: Wedge side vector #2 z component.
        v3x: Wedge height vector x component.
        v3y: Wedge height vector y component.
        v3z: Wedge height vector z component.
    """

    vx: str | float | types.Real
    vy: str | float | types.Real
    vz: str | float | types.Real
    v1x: str | float | types.Real
    v1y: str | float | types.Real
    v1z: str | float | types.Real
    v2x: str | float | types.Real
    v2y: str | float | types.Real
    v2z: str | float | types.Real
    v3x: str | float | types.Real
    v3y: str | float | types.Real
    v3z: str | float | types.Real

    def build(self):
        """
        Builds ``WedBuilder`` into ``Wed``.

        Returns:
            ``Wed`` for ``WedBuilder``.
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

        v3x = self.v3x
        if isinstance(self.v3x, types.Real):
            v3x = self.v3x
        elif isinstance(self.v3x, float) or isinstance(self.v3x, int):
            v3x = types.Real(self.v3x)
        elif isinstance(self.v3x, str):
            v3x = types.Real.from_mcnp(self.v3x)

        v3y = self.v3y
        if isinstance(self.v3y, types.Real):
            v3y = self.v3y
        elif isinstance(self.v3y, float) or isinstance(self.v3y, int):
            v3y = types.Real(self.v3y)
        elif isinstance(self.v3y, str):
            v3y = types.Real.from_mcnp(self.v3y)

        v3z = self.v3z
        if isinstance(self.v3z, types.Real):
            v3z = self.v3z
        elif isinstance(self.v3z, float) or isinstance(self.v3z, int):
            v3z = types.Real(self.v3z)
        elif isinstance(self.v3z, str):
            v3z = types.Real.from_mcnp(self.v3z)

        return Wed(
            vx=vx,
            vy=vy,
            vz=vz,
            v1x=v1x,
            v1y=v1y,
            v1z=v1z,
            v2x=v2x,
            v2y=v2y,
            v2z=v2z,
            v3x=v3x,
            v3y=v3y,
            v3z=v3z,
        )
