import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser
from ...utils import _visualization


class SurfaceOption_Ell(_option.SurfaceOption_, keyword='ell'):
    """
    Represents INP surface card ell options.

    Attributes:
        v1x: Ellipsoid focus #1 or center x component.
        v1y: Ellipsoid focus #1 or center y component.
        v1z: Ellipsoid focus #1 or center z component.
        v2x: Ellipsoid focus #2 or major axis x component.
        v2y: Ellipsoid focus #2 or major axis y component.
        v2z: Ellipsoid focus #2 or major axis z component.
        rm: Ellipsoid major/minor axis radius length.
    """

    _REGEX = re.compile(r'\Aell( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)\Z')

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
        Initializes ``SurfaceOption_Ell``.

        Parameters:
            v1x: Ellipsoid focus #1 or center x component.
            v1y: Ellipsoid focus #1 or center y component.
            v1z: Ellipsoid focus #1 or center z component.
            v2x: Ellipsoid focus #2 or major axis x component.
            v2y: Ellipsoid focus #2 or major axis y component.
            v2z: Ellipsoid focus #2 or major axis z component.
            rm: Ellipsoid major/minor axis radius length.

        Returns:
            ``SurfaceOption_Ell``.

        Raises:
            InpError: SYNTAX_OPTION_VALUE.
        """

        if v1x is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, v1x)
        if v1y is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, v1y)
        if v1z is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, v1z)
        if v2x is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, v2x)
        if v2y is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, v2y)
        if v2z is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, v2z)
        if rm is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, rm)

        self.value: typing.Final[tuple[any]] = types._Tuple([v1x, v1y, v1z, v2x, v2y, v2z, rm])
        self.v1x: typing.Final[types.Real] = v1x
        self.v1y: typing.Final[types.Real] = v1y
        self.v1z: typing.Final[types.Real] = v1z
        self.v2x: typing.Final[types.Real] = v2x
        self.v2y: typing.Final[types.Real] = v2y
        self.v2z: typing.Final[types.Real] = v2z
        self.rm: typing.Final[types.Real] = rm

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SurfaceOption_Ell`` from INP.

        Parameters:
            source: INP surface card option.

        Returns:
            ``SurfaceOption_Ell``.

        Raises:
            InpError: SYNTAX_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SurfaceOption_Ell._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        v1x = types.Real.from_mcnp(tokens[1])
        v1y = types.Real.from_mcnp(tokens[2])
        v1z = types.Real.from_mcnp(tokens[3])
        v2x = types.Real.from_mcnp(tokens[4])
        v2y = types.Real.from_mcnp(tokens[5])
        v2z = types.Real.from_mcnp(tokens[6])
        rm = types.Real.from_mcnp(tokens[7])

        return SurfaceOption_Ell(v1x, v1y, v1z, v2x, v2y, v2z, rm)

    def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Ell``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Ell``.
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
