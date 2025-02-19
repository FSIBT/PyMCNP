import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser
from ...utils import _visualization


class SurfaceOption_C_z(_option.SurfaceOption_, keyword='c/z'):
    """
    Represents INP surface card c/z options.

    Attributes:
        x: Parallel-to-z-axis cylinder center x component.
        y: Parallel-to-z-axis cylinder center y component.
        r: Parallel-to-z-axis cylinder radius.
    """

    _REGEX = re.compile(r'\Ac/z( \S+)( \S+)( \S+)\Z')

    def __init__(self, x: types.Real, y: types.Real, r: types.Real):
        """
        Initializes ``SurfaceOption_C_z``.

        Parameters:
            x: Parallel-to-z-axis cylinder center x component.
            y: Parallel-to-z-axis cylinder center y component.
            r: Parallel-to-z-axis cylinder radius.

        Returns:
            ``SurfaceOption_C_z``.

        Raises:
            InpError: SYNTAX_OPTION_VALUE.
        """

        if x is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, x)
        if y is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, y)
        if r is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, r)

        self.value: typing.Final[tuple[any]] = types._Tuple([x, y, r])
        self.x: typing.Final[types.Real] = x
        self.y: typing.Final[types.Real] = y
        self.r: typing.Final[types.Real] = r

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SurfaceOption_C_z`` from INP.

        Parameters:
            source: INP surface card option.

        Returns:
            ``SurfaceOption_C_z``.

        Raises:
            InpError: SYNTAX_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SurfaceOption_C_z._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        x = types.Real.from_mcnp(tokens[1])
        y = types.Real.from_mcnp(tokens[2])
        r = types.Real.from_mcnp(tokens[3])

        return SurfaceOption_C_z(x, y, r)

    def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_C_z``.
        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_C_z``.
        """

        vis = _visualization.McnpVisualization.get_cylinder_unbounded(self.r.value)
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x.value, self.y.value, 0))

        return vis.data
