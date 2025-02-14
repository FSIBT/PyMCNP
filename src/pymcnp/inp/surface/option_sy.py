import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser
from ...utils import _visualization


class SurfaceOption_Sy(_option.SurfaceOption_, keyword='sy'):
    """
    Represents INP surface card sy options.

    Attributes:
        y: On-y-axis sphere center y component.
        r: On-y-axis sphere radius.
    """

    _REGEX = re.compile(r'\Asy( \S+)( \S+)\Z')

    def __init__(self, y: types.Real, r: types.Real):
        """
        Initializes ``SurfaceOption_Sy``.

        Parameters:
            y: On-y-axis sphere center y component.
            r: On-y-axis sphere radius.

        Returns:
            ``SurfaceOption_Sy``.

        Raises:
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
        """

        if y is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, y)
        if r is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, r)

        self.value: typing.Final[tuple[any]] = types._Tuple([y, r])
        self.y: typing.Final[types.Real] = y
        self.r: typing.Final[types.Real] = r

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SurfaceOption_Sy`` from INP.

        Parameters:
            source: INP surface card option.

        Returns:
            ``SurfaceOption_Sy``.

        Raises:
            McnpError: SYNTAX_SURFACE_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SurfaceOption_Sy._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SURFACE_OPTION, source)

        y = types.Real.from_mcnp(tokens[1])
        r = types.Real.from_mcnp(tokens[2])

        return SurfaceOption_Sy(y, r)

    def to_pyvista(self):
        """
        Generates ``pyvista[.]PolyData`` from ``SurfaceOption_Sy``.

        Returns:
            ``pyvista[.]PolyData`` for ``SurfaceOption_Sy``
        """

        vis = _visualization.PyMcnpVisualization.get_sphere(self.r.value)
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(0, self.y.value, 0))

        return vis.data
