import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser
from ...utils import _visualization


class SurfaceOption_C_x(_option.SurfaceOption_, keyword='c/x'):
    """
    Represents INP surface card c/x options.

    Attributes:
        y: Parallel-to-x-axis cylinder center y component.
        z: Parallel-to-x-axis cylinder center z component.
        r: Parallel-to-x-axis cylinder radius.
    """

    _REGEX = re.compile(r'\Ac/x( \S+)( \S+)( \S+)\Z')

    def __init__(self, y: types.Real, z: types.Real, r: types.Real):
        """
        Initializes ``SurfaceOption_C_x``.

        Parameters:
            y: Parallel-to-x-axis cylinder center y component.
            z: Parallel-to-x-axis cylinder center z component.
            r: Parallel-to-x-axis cylinder radius.

        Returns:
            ``SurfaceOption_C_x``.

        Raises:
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
        """

        if y is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, y)
        if z is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, z)
        if r is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, r)

        self.value: typing.Final[tuple[any]] = types._Tuple([y, z, r])
        self.y: typing.Final[types.Real] = y
        self.z: typing.Final[types.Real] = z
        self.r: typing.Final[types.Real] = r

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SurfaceOption_C_x`` from INP.

        Parameters:
            source: INP surface card option.

        Returns:
            ``SurfaceOption_C_x``.

        Raises:
            McnpError: SYNTAX_SURFACE_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SurfaceOption_C_x._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SURFACE_OPTION, source)

        y = types.Real.from_mcnp(tokens[1])
        z = types.Real.from_mcnp(tokens[2])
        r = types.Real.from_mcnp(tokens[3])

        return SurfaceOption_C_x(y, z, r)

    def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_C_x``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_C_x``.
        """

        vis = _visualization.PyMcnpVisualization.get_cylinder_unbounded(self.r.value)
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(0, self.y.value, self.z.value))

        return vis.data
