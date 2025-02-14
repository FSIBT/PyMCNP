import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser
from ...utils import _visualization


class SurfaceOption_Cx(_option.SurfaceOption_, keyword='cx'):
    """
    Represents INP surface card cx options.

    Attributes:
        r: On-x-axis cylinder radius.
    """

    _REGEX = re.compile(r'\Acx( \S+)\Z')

    def __init__(self, r: types.Real):
        """
        Initializes ``SurfaceOption_Cx``.

        Parameters:
            r: On-x-axis cylinder radius.

        Returns:
            ``SurfaceOption_Cx``.

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
        Generates ``SurfaceOption_Cx`` from INP.

        Parameters:
            source: INP surface card option.

        Returns:
            ``SurfaceOption_Cx``.

        Raises:
            McnpError: SYNTAX_SURFACE_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SurfaceOption_Cx._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SURFACE_OPTION, source)

        r = types.Real.from_mcnp(tokens[1])

        return SurfaceOption_Cx(r)

    def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Cx``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Cx``.
        """

        vis = _visualization.PyMcnpVisualization.get_cylinder_unbounded(self.r.value)
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))

        return vis.data
