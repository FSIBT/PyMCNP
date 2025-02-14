import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser
from ...utils import _visualization


class SurfaceOption_Cy(_option.SurfaceOption_, keyword='cy'):
    """
    Represents INP surface card cy options.

    Attributes:
        r: On-y-axis cylinder radius.
    """

    _REGEX = re.compile(r'\Acy( \S+)\Z')

    def __init__(self, r: types.Real):
        """
        Initializes ``SurfaceOption_Cy``.

        Parameters:
            r: On-y-axis cylinder radius.

        Returns:
            ``SurfaceOption_Cy``.

        Raises:
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
        """

        if r is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, r)

        self.value: typing.Final[tuple[any]] = types._Tuple([r])
        self.r: typing.Final[types.Real] = r

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SurfaceOption_Cy`` from INP.

        Parameters:
            source: INP surface card option.

        Returns:
            ``SurfaceOption_Cy``.

        Raises:
            McnpError: SYNTAX_SURFACE_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SurfaceOption_Cy._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SURFACE_OPTION, source)

        r = types.Real.from_mcnp(tokens[1])

        return SurfaceOption_Cy(r)

    def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Cy``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Cy``.
        """

        vis = _visualization.PyMcnpVisualization.get_cylinder_unbounded(self.r.value)
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))

        return vis.data
