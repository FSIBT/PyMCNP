import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser
from ...utils import _visualization


class SurfaceOption_Cz(_option.SurfaceOption_, keyword='cz'):
    """
    Represents INP surface card cz options.

    Attributes:
        r: On-z-axis cylinder radius.
    """

    _REGEX = re.compile(r'\Acz( \S+)\Z')

    def __init__(self, r: types.Real):
        """
        Initializes ``SurfaceOption_Cz``.

        Parameters:
            r: On-z-axis cylinder radius.

        Returns:
            ``SurfaceOption_Cz``.

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
        Generates ``SurfaceOption_Cz`` from INP.

        Parameters:
            source: INP surface card option.

        Returns:
            ``SurfaceOption_Cz``.

        Raises:
            McnpError: SYNTAX_SURFACE_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SurfaceOption_Cz._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SURFACE_OPTION, source)

        r = types.Real.from_mcnp(tokens[1])

        return SurfaceOption_Cz(r)

    def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Cz``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Cz``.
        """

        vis = _visualization.PyMcnpVisualization.get_cylinder_unbounded(self.r.value)

        return vis.data
