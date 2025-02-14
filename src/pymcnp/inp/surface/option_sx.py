import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser
from ...utils import _visualization


class SurfaceOption_Sx(_option.SurfaceOption_, keyword='sx'):
    """
    Represents INP surface card sx options.

    Attributes:
        x: On-x-axis sphere center x component.
        r: On-x-axis sphere radius.
    """

    _REGEX = re.compile(r'\Asx( \S+)( \S+)\Z')

    def __init__(self, x: types.Real, r: types.Real):
        """
        Initializes ``SurfaceOption_Sx``.

        Parameters:
            x: On-x-axis sphere center x component.
            r: On-x-axis sphere radius.

        Returns:
            ``SurfaceOption_Sx``.

        Raises:
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
        """

        if x is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, x)
        if r is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, r)

        self.value: typing.Final[tuple[any]] = types._Tuple([x, r])
        self.x: typing.Final[types.Real] = x
        self.r: typing.Final[types.Real] = r

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SurfaceOption_Sx`` from INP.

        Parameters:
            source: INP surface card option.

        Returns:
            ``SurfaceOption_Sx``.

        Raises:
            McnpError: SYNTAX_SURFACE_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SurfaceOption_Sx._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SURFACE_OPTION, source)

        x = types.Real.from_mcnp(tokens[1])
        r = types.Real.from_mcnp(tokens[2])

        return SurfaceOption_Sx(x, r)

    def to_pyvista(self):
        """
        Generates ``pyvista[.]PolyData`` from ``SurfaceOption_Sx``.

        Returns:
            ``pyvista[.]PolyData`` for ``SurfaceOption_Sx``
        """

        vis = _visualization.PyMcnpVisualization.get_sphere(self.r.value)
        vis = vis.add_translation(_visualization.Vector(self.x.value, 0, 0))

        return vis.data
