import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Wed(SurfaceOption_, keyword='wed'):
    """
    Represents INP wed elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
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
        rf'wed( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
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
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if vx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, vx)
        if vy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, vy)
        if vz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, vz)
        if v1x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, v1x)
        if v1y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, v1y)
        if v1z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, v1z)
        if v2x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, v2x)
        if v2y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, v2y)
        if v2z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, v2z)
        if v3x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, v3x)
        if v3y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, v3y)
        if v3z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, v3z)

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
