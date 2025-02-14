import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser
from ...utils import _visualization


class SurfaceOption_Pz(_option.SurfaceOption_, keyword='pz'):
    """
    Represents INP surface card pz options.

    Attributes:
        d: Normal-to-the-z-axis plane D coefficent.
    """

    _REGEX = re.compile(r'\Apz( \S+)\Z')

    def __init__(self, d: types.Real):
        """
        Initializes ``SurfaceOption_Pz``.

        Parameters:
            d: Normal-to-the-z-axis plane D coefficent.

        Returns:
            ``SurfaceOption_Pz``.

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
        Generates ``SurfaceOption_Pz`` from INP.

        Parameters:
            source: INP surface card option.

        Returns:
            ``SurfaceOption_Pz``.

        Raises:
            McnpError: SYNTAX_SURFACE_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SurfaceOption_Pz._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SURFACE_OPTION, source)

        d = types.Real.from_mcnp(tokens[1])

        return SurfaceOption_Pz(d)

    def to_pyvista(self):
        """
        Generates ``pyvista[.]PolyData`` from ``SurfaceOption_Pz``.

        Returns:
            ``pyvista[.]PolyData`` for ``SurfaceOption_Pz``
        """

        vis = _visualization.PyMcnpVisualization.get_plane(0, 0, 1, self.d.value)

        return vis.data
