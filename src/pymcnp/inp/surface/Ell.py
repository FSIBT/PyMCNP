import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Ell(SurfaceOption_, keyword='ell'):
    """
    Represents INP ell elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'v1x': types.Real,
        'v1y': types.Real,
        'v1z': types.Real,
        'v2x': types.Real,
        'v2y': types.Real,
        'v2z': types.Real,
        'rm': types.Real,
    }

    _REGEX = re.compile(
        rf'ell( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
    )

    def __init__(
        self,
        v1x: types.Real,
        v1y: types.Real,
        v1z: types.Real,
        v2x: types.Real,
        v2y: types.Real,
        v2z: types.Real,
        rm: types.Real,
    ):
        """
        Initializes ``Ell``.

        Parameters:
            v1x: Ellipsoid focus #1 or center x component.
            v1y: Ellipsoid focus #1 or center y component.
            v1z: Ellipsoid focus #1 or center z component.
            v2x: Ellipsoid focus #2 or major axis x component.
            v2y: Ellipsoid focus #2 or major axis y component.
            v2z: Ellipsoid focus #2 or major axis z component.
            rm: Ellipsoid major/minor axis radius length.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

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
        if rm is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, rm)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                v1x,
                v1y,
                v1z,
                v2x,
                v2y,
                v2z,
                rm,
            ]
        )

        self.v1x: typing.Final[types.Real] = v1x
        self.v1y: typing.Final[types.Real] = v1y
        self.v1z: typing.Final[types.Real] = v1z
        self.v2x: typing.Final[types.Real] = v2x
        self.v2y: typing.Final[types.Real] = v2y
        self.v2z: typing.Final[types.Real] = v2z
        self.rm: typing.Final[types.Real] = rm

        def to_pyvista(self):
            """
            Generates ``pyvista.PolyData`` from ``Ell``.

            Returns:
                ``pyvista.PolyData`` for ``Ell``.
            """

            v1 = _visualization.Vector(self.v1x.value, self.v1y.value, self.v1z.value)
            v2 = _visualization.Vector(self.v2x.value, self.v2y.value, self.v2z.value)

            if self.rm > 0:
                center = _visualization.Vector(
                    (v2 - v1).x / 2 + v1.x, (v2 - v1).y / 2 + v1.y, (v2 - v1).z / 2 + v1.z
                )
                major_length = self.rm.value
                minor_length = 2 * (((major_length / 2) ** 2 - ((v2 - v1).norm() / 2) ** 2) ** 0.5)
                cross = (v2 - v1) * _visualization.Vector(1, 0, 0)
                angle = (v2 - v1) & _visualization.Vector(1, 0, 0)
            elif self.rm < 0:
                center = v1
                major_length = v2.norm()
                minor_length = -self.rm.value
                cross = v2 * _visualization.Vector(1, 0, 0)
                angle = v2 & _visualization.Vector(1, 0, 0)

            vis = _visualization.McnpVisualization.get_ellipsoid(major_length, minor_length)
            vis = vis.add_rotation(cross, angle, (0, 0, 0))
            vis = vis.add_translation(center)

            return vis.data
