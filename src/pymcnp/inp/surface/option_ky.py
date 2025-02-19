import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser
from ...utils import _visualization


class SurfaceOption_Ky(_option.SurfaceOption_, keyword='ky'):
    """
    Represents INP surface card ky options.

    Attributes:
        y: On-y-axis cone center y component.
        t_squared: On-y-axis cone t^2 coefficent.
        plusminus_1: On-y-axis cone sheet selector.
    """

    _REGEX = re.compile(r'\Aky( \S+)( \S+)( \S+)\Z')

    def __init__(self, y: types.Real, t_squared: types.Real, plusminus_1: types.Real):
        """
        Initializes ``SurfaceOption_Ky``.

        Parameters:
            y: On-y-axis cone center y component.
            t_squared: On-y-axis cone t^2 coefficent.
            plusminus_1: On-y-axis cone sheet selector.

        Returns:
            ``SurfaceOption_Ky``.

        Raises:
            InpError: SYNTAX_OPTION_VALUE.
        """

        if y is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, y)
        if t_squared is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, t_squared)
        if plusminus_1 is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, plusminus_1)

        self.value: typing.Final[tuple[any]] = types._Tuple([y, t_squared, plusminus_1])
        self.y: typing.Final[types.Real] = y
        self.t_squared: typing.Final[types.Real] = t_squared
        self.plusminus_1: typing.Final[types.Real] = plusminus_1

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SurfaceOption_Ky`` from INP.

        Parameters:
            source: INP surface card option.

        Returns:
            ``SurfaceOption_Ky``.

        Raises:
            InpError: SYNTAX_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SurfaceOption_Ky._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        y = types.Real.from_mcnp(tokens[1])
        t_squared = types.Real.from_mcnp(tokens[2])
        plusminus_1 = types.Real.from_mcnp(tokens[3])

        return SurfaceOption_Ky(y, t_squared, plusminus_1)

    def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Ky``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Ky``.
        """

        vis = _visualization.McnpVisualization.get_cone_quadratic(
            self.t_squared.value ** (1 / 2), self.plusminus_1.value
        )
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(0, self.y.value, 0))

        return vis.data
