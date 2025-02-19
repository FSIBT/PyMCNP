import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser
from ...utils import _visualization


class SurfaceOption_Kz(_option.SurfaceOption_, keyword='kz'):
    """
    Represents INP surface card kz options.

    Attributes:
        z: On-z-axis cone center z component.
        t_squared: On-z-axis cone t^2 coefficent.
        plusminus_1: On-z-axis cone sheet selector.
    """

    _REGEX = re.compile(r'\Akz( \S+)( \S+)( \S+)\Z')

    def __init__(self, z: types.Real, t_squared: types.Real, plusminus_1: types.Real):
        """
        Initializes ``SurfaceOption_Kz``.

        Parameters:
            z: On-z-axis cone center z component.
            t_squared: On-z-axis cone t^2 coefficent.
            plusminus_1: On-z-axis cone sheet selector.

        Returns:
            ``SurfaceOption_Kz``.

        Raises:
            InpError: SYNTAX_OPTION_VALUE.
        """

        if z is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, z)
        if t_squared is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, t_squared)
        if plusminus_1 is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, plusminus_1)

        self.value: typing.Final[tuple[any]] = types._Tuple([z, t_squared, plusminus_1])
        self.z: typing.Final[types.Real] = z
        self.t_squared: typing.Final[types.Real] = t_squared
        self.plusminus_1: typing.Final[types.Real] = plusminus_1

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SurfaceOption_Kz`` from INP.

        Parameters:
            source: INP surface card option.

        Returns:
            ``SurfaceOption_Kz``.

        Raises:
            InpError: SYNTAX_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SurfaceOption_Kz._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        z = types.Real.from_mcnp(tokens[1])
        t_squared = types.Real.from_mcnp(tokens[2])
        plusminus_1 = types.Real.from_mcnp(tokens[3])

        return SurfaceOption_Kz(z, t_squared, plusminus_1)

    def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``SurfaceOption_Kz``.

        Returns:
            ``pyvista.PolyData`` for ``SurfaceOption_Kz``.
        """

        vis = _visualization.McnpVisualization.get_cone_quadratic(
            self.t_squared.value ** (1 / 2), self.plusminus_1.value
        )
        vis = vis.add_translation(_visualization.Vector(0, 0, self.z.value))

        return vis.data
