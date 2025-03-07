import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Rec(SurfaceOption_, keyword='rec'):
    """
    Represents INP rec elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

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
        rf'rec( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
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
        v2y: types.Real,
        v2z: types.Real,
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
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if vx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, vx)
        if vy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, vy)
        if vz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, vz)
        if hx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, hx)
        if hy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, hy)
        if hz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, hz)
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

        def to_pyvista(self):
            """
            Generates ``pyvista.PolyData`` from ``Rec``.

            Returns:
                ``pyvista.PolyData`` for ``Rec``
            """

            v = _visualization.Vector(self.vx.value, self.vy.value, self.vz.value)
            h = _visualization.Vector(self.hx.value, self.hy.value, self.hz.value)
            v1 = _visualization.Vector(self.v1x.value, self.v1y.value, self.v1z.value)
            v2 = _visualization.Vector(self.v2x.value, self.v2y.value, self.v2z.value)

            cross = v * _visualization.Vector(0, 0, 1)
            angle = v & _visualization.Vector(0, 0, 1)

            vis = _visualization.McnpVisualization.get_cylinder_ellipse(
                h.norm(), v1.norm(), v2.norm()
            )
            vis = vis.add_rotation(cross, angle, (0, 0, 0))
            vis = vis.add_translation(v)

            return vis.data
