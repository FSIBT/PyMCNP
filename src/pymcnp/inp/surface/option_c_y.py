import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser
from ...utils import _visualization


class SurfaceOption_C_y(_option.SurfaceOption_, keyword='c/y'):
    """
    Represents INP surface card c/y options.

    Attributes:
        x: Parallel-to-y-axis cylinder center x component.
        z: Parallel-to-y-axis cylinder center z component.
        r: Parallel-to-y-axis cylinder radius.
    """

    _REGEX = re.compile(r'\Ac/y( \S+)( \S+)( \S+)\Z')

    def __init__(self, x: types.Real, z: types.Real, r: types.Real):
        """
        Initializes ``SurfaceOption_C_y``.

        Parameters:
            x: Parallel-to-y-axis cylinder center x component.
            z: Parallel-to-y-axis cylinder center z component.
            r: Parallel-to-y-axis cylinder radius.

        Returns:
            ``SurfaceOption_C_y``.

        Raises:
            InpError: SYNTAX_OPTION_VALUE.
        """

        if x is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, x)
        if z is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, z)
        if r is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, r)

        self.value: typing.Final[tuple[any]] = types._Tuple([x, z, r])
        self.x: typing.Final[types.Real] = x
        self.z: typing.Final[types.Real] = z
        self.r: typing.Final[types.Real] = r

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SurfaceOption_C_y`` from INP.

        Parameters:
            source: INP surface card option.

        Returns:
            ``SurfaceOption_C_y``.

        Raises:
            InpError: SYNTAX_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SurfaceOption_C_y._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        x = types.Real.from_mcnp(tokens[1])
        z = types.Real.from_mcnp(tokens[2])
        r = types.Real.from_mcnp(tokens[3])

        return SurfaceOption_C_y(x, z, r)

    def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_C_y``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_C_y``.
        """

        vis = _visualization.McnpVisualization.get_cylinder_unbounded(self.r.value)
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x.value, 0, self.z.value))

        return vis.data
