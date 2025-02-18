import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser
from ...utils import _visualization


class SurfaceOption_K_x(_option.SurfaceOption_, keyword='k/x'):
    """
    Represents INP surface card k/x options.

    Attributes:
        x: Parallel-to-x-axis cone center x component.
        y: Parallel-to-x-axis cone center y component.
        z: Parallel-to-x-axis cone center z component.
        t_squared: Parallel-to-x-axis cone t^2 coefficent.
        plusminus_1: Parallel-to-x-axis cone sheet selector.
    """

    _REGEX = re.compile(r'\Ak/x( \S+)( \S+)( \S+)( \S+)( \S+)\Z')

    def __init__(
        self,
        x: types.Real,
        y: types.Real,
        z: types.Real,
        t_squared: types.Real,
        plusminus_1: types.Real,
    ):
        """
        Initializes ``SurfaceOption_K_x``.

        Parameters:
            x: Parallel-to-x-axis cone center x component.
            y: Parallel-to-x-axis cone center y component.
            z: Parallel-to-x-axis cone center z component.
            t_squared: Parallel-to-x-axis cone t^2 coefficent.
            plusminus_1: Parallel-to-x-axis cone sheet selector.

        Returns:
            ``SurfaceOption_K_x``.

        Raises:
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
        """

        if x is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, x)
        if y is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, y)
        if z is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, z)
        if t_squared is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, t_squared)
        if plusminus_1 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, plusminus_1)

        self.value: typing.Final[tuple[any]] = types._Tuple([x, y, z, t_squared, plusminus_1])
        self.x: typing.Final[types.Real] = x
        self.y: typing.Final[types.Real] = y
        self.z: typing.Final[types.Real] = z
        self.t_squared: typing.Final[types.Real] = t_squared
        self.plusminus_1: typing.Final[types.Real] = plusminus_1

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SurfaceOption_K_x`` from INP.

        Parameters:
            source: INP surface card option.

        Returns:
            ``SurfaceOption_K_x``.

        Raises:
            McnpError: SYNTAX_SURFACE_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SurfaceOption_K_x._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SURFACE_OPTION, source)

        x = types.Real.from_mcnp(tokens[1])
        y = types.Real.from_mcnp(tokens[2])
        z = types.Real.from_mcnp(tokens[3])
        t_squared = types.Real.from_mcnp(tokens[4])
        plusminus_1 = types.Real.from_mcnp(tokens[5])

        return SurfaceOption_K_x(x, y, z, t_squared, plusminus_1)

    def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_K_x``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_K_x``.
        """

        vis = _visualization.McnpVisualization.get_cone_quadratic(
            self.t_squared.value ** (1 / 2), self.plusminus_1.value
        )
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x.value, self.y.value, self.z.value))

        return vis.data
