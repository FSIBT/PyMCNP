import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser
from ...utils import _visualization


class SurfaceOption_Px(_option.SurfaceOption_, keyword='px'):
    """
    Represents INP surface card px options.

    Attributes:
        d: Normal-to-the-x-axis plane D coefficent.
    """

    _REGEX = re.compile(r'\Apx( \S+)\Z')

    def __init__(self, d: types.Real):
        """
        Initializes ``SurfaceOption_Px``.

        Parameters:
            d: Normal-to-the-x-axis plane D coefficent.

        Returns:
            ``SurfaceOption_Px``.

        Raises:
            InpError: SYNTAX_OPTION_VALUE.
        """

        if d is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, d)

        self.value: typing.Final[tuple[any]] = types._Tuple([d])
        self.d: typing.Final[types.Real] = d

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SurfaceOption_Px`` from INP.

        Parameters:
            source: INP surface card option.

        Returns:
            ``SurfaceOption_Px``.

        Raises:
            InpError: SYNTAX_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SurfaceOption_Px._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        d = types.Real.from_mcnp(tokens[1])

        return SurfaceOption_Px(d)

    def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Px``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Px``
        """

        vis = _visualization.McnpVisualization.get_plane(1, 0, 0, self.d.value)
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))

        return vis.data
