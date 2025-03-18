import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class K_x(SurfaceOption_, keyword='k/x'):
    """
    Represents INP k/x elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'x': types.Real,
        'y': types.Real,
        'z': types.Real,
        't_squared': types.Real,
        'plusminus_1': types.Real,
    }

    _REGEX = re.compile(
        rf'k/x( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
    )

    def __init__(
        self,
        x: types.Real,
        y: types.Real,
        z: types.Real,
        t_squared: types.Real,
        plusminus_1: types.Real,
    ):
        """
        Initializes ``K_x``.

        Parameters:
            x: Parallel-to-x-axis cone center x component.
            y: Parallel-to-x-axis cone center y component.
            z: Parallel-to-x-axis cone center z component.
            t_squared: Parallel-to-x-axis cone t^2 coefficent.
            plusminus_1: Parallel-to-x-axis cone sheet selector.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x)
        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, y)
        if z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, z)
        if t_squared is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, t_squared)
        if plusminus_1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, plusminus_1)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x,
                y,
                z,
                t_squared,
                plusminus_1,
            ]
        )

        self.x: typing.Final[types.Real] = x
        self.y: typing.Final[types.Real] = y
        self.z: typing.Final[types.Real] = z
        self.t_squared: typing.Final[types.Real] = t_squared
        self.plusminus_1: typing.Final[types.Real] = plusminus_1

    def draw(self):
        """
        Generates ``Visualization`` from ``K_x``.

        Returns:
            ``pyvista.PolyData`` for ``K_x``.
        """

        vis = _visualization.Visualization.get_cone_quadratic(
            self.t_squared.value ** (1 / 2), self.plusminus_1.value
        )
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x.value, self.y.value, self.z.value))

        return vis
