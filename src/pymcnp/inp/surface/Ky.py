import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Ky(SurfaceOption_, keyword='ky'):
    """
    Represents INP ky elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'y': types.Real,
        't_squared': types.Real,
        'plusminus_1': types.Real,
    }

    _REGEX = re.compile(
        rf'ky( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
    )

    def __init__(self, y: types.Real, t_squared: types.Real, plusminus_1: types.Real):
        """
        Initializes ``Ky``.

        Parameters:
            y: On-y-axis cone center y component.
            t_squared: On-y-axis cone t^2 coefficent.
            plusminus_1: On-y-axis cone sheet selector.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, y)
        if t_squared is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, t_squared)
        if plusminus_1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, plusminus_1)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                y,
                t_squared,
                plusminus_1,
            ]
        )

        self.y: typing.Final[types.Real] = y
        self.t_squared: typing.Final[types.Real] = t_squared
        self.plusminus_1: typing.Final[types.Real] = plusminus_1

    def draw(self):
        """
        Generates ``Visualization`` from ``Ky``.

        Returns:
            ``pyvista.PolyData`` for ``Ky``.
        """

        vis = _visualization.Visualization.get_cone_quadratic(
            self.t_squared.value ** (1 / 2), self.plusminus_1.value
        )
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(0, self.y.value, 0))

        return vis
