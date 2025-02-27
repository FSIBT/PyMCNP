import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class K_y(SurfaceOption_, keyword='k/y'):
    """
    Represents INP k/y elements.

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

    _REGEX = re.compile(r'k/y( \S+)( \S+)( \S+)( \S+)( \S+)')

    def __init__(
        self,
        x: types.Real,
        y: types.Real,
        z: types.Real,
        t_squared: types.Real,
        plusminus_1: types.Real,
    ):
        """
        Initializes ``K_y``.

        Parameters:
            x: Parallel-to-y-axis cone center x component.
            y: Parallel-to-y-axis cone center y component.
            z: Parallel-to-y-axis cone center z component.
            t_squared: Parallel-to-y-axis cone t^2 coefficent.
            plusminus_1: Parallel-to-y-axis cone sheet selector.

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

        def to_pyvista(self):
            """
            Generates ``pyvista.PolyData`` from ``K_y``.

            Returns:
                ``pyvista.PolyData`` for ``K_y``.
            """

            vis = _visualization.McnpVisualization.get_cone_quadratic(
                self.t_squared.value ** (1 / 2), self.plusminus_1.value
            )
            vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))
            vis = vis.add_translation(
                _visualization.Vector(self.x.value, self.y.value, self.z.value)
            )

            return vis.data
