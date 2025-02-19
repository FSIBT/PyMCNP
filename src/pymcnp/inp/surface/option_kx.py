import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser
from ...utils import _visualization


class SurfaceOption_Kx(_option.SurfaceOption_, keyword='kx'):
    """
    Represents INP surface card kx options.

    Attributes:
        x: On-x-axis cone center x component.
        t_squared: On-x-axis cone t^2 coefficent.
        plusminus_1: On-x-axis cone sheet selector.
    """

    _REGEX = re.compile(r'\Akx( \S+)( \S+)( \S+)\Z')

    def __init__(self, x: types.Real, t_squared: types.Real, plusminus_1: types.Real):
        """
        Initializes ``SurfaceOption_Kx``.

        Parameters:
            x: On-x-axis cone center x component.
            t_squared: On-x-axis cone t^2 coefficent.
            plusminus_1: On-x-axis cone sheet selector.

        Returns:
            ``SurfaceOption_Kx``.

        Raises:
            InpError: SYNTAX_OPTION_VALUE.
        """

        if x is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, x)
        if t_squared is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, t_squared)
        if plusminus_1 is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, plusminus_1)

        self.value: typing.Final[tuple[any]] = types._Tuple([x, t_squared, plusminus_1])
        self.x: typing.Final[types.Real] = x
        self.t_squared: typing.Final[types.Real] = t_squared
        self.plusminus_1: typing.Final[types.Real] = plusminus_1

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SurfaceOption_Kx`` from INP.

        Parameters:
            source: INP surface card option.

        Returns:
            ``SurfaceOption_Kx``.

        Raises:
            InpError: SYNTAX_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SurfaceOption_Kx._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        x = types.Real.from_mcnp(tokens[1])
        t_squared = types.Real.from_mcnp(tokens[2])
        plusminus_1 = types.Real.from_mcnp(tokens[3])

        return SurfaceOption_Kx(x, t_squared, plusminus_1)

    def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Kx``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Kx``.
        """

        vis = _visualization.McnpVisualization.get_cone_quadratic(
            self.t_squared.value ** (1 / 2), self.plusminus_1.value
        )
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x.value, 0, 0))

        return vis.data
