import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser
from ...utils import _visualization


class SurfaceOption_So(_option.SurfaceOption_, keyword='so'):
    """
    Represents INP surface card so options.

    Attributes:
        r: Origin-centered sphere radius.
    """

    _REGEX = re.compile(r'\Aso( \S+)\Z')

    def __init__(self, r: types.Real):
        """
        Initializes ``SurfaceOption_So``.

        Parameters:
            r: Origin-centered sphere radius.

        Returns:
            ``SurfaceOption_So``.

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
        Generates ``SurfaceOption_So`` from INP.

        Parameters:
            source: INP surface card option.

        Returns:
            ``SurfaceOption_So``.

        Raises:
            McnpError: SYNTAX_SURFACE_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SurfaceOption_So._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SURFACE_OPTION, source)

        r = types.Real.from_mcnp(tokens[1])

        return SurfaceOption_So(r)

    def to_pyvista(self):
        """
        Generates ``pyvista[.]PolyData`` from ``SurfaceOption_So``.

        Returns:
            ``pyvista[.]PolyData`` for ``SurfaceOption_So``
        """

        vis = _visualization.PyMcnpVisualization.get_sphere(self.r.value)

        return vis.data
