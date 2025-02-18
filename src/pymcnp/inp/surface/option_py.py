import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser
from ...utils import _visualization


class SurfaceOption_Py(_option.SurfaceOption_, keyword='py'):
    """
    Represents INP surface card py options.

    Attributes:
        d: Normal-to-the-y-axis plane D coefficent.
    """

    _REGEX = re.compile(r'\Apy( \S+)\Z')

    def __init__(self, d: types.Real):
        """
        Initializes ``SurfaceOption_Py``.

        Parameters:
            d: Normal-to-the-y-axis plane D coefficent.

        Returns:
            ``SurfaceOption_Py``.

        Raises:
            McnpError: SEMANTICS_SURFACE_OPTION_VALUE.
        """

        if d is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION_VALUE, d)

        self.value: typing.Final[tuple[any]] = types._Tuple([d])
        self.d: typing.Final[types.Real] = d

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SurfaceOption_Py`` from INP.

        Parameters:
            source: INP surface card option.

        Returns:
            ``SurfaceOption_Py``.

        Raises:
            McnpError: SYNTAX_SURFACE_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SurfaceOption_Py._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SURFACE_OPTION, source)

        d = types.Real.from_mcnp(tokens[1])

        return SurfaceOption_Py(d)

    def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Py``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Py``
        """

        vis = _visualization.McnpVisualization.get_plane(0, 1, 0, self.d.value)
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))

        return vis.data
