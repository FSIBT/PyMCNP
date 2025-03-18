import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Kz(SurfaceOption_, keyword='kz'):
    """
    Represents INP kz elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'z': types.Real,
        't_squared': types.Real,
        'plusminus_1': types.Real,
    }

    _REGEX = re.compile(
        rf'kz( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
    )

    def __init__(self, z: types.Real, t_squared: types.Real, plusminus_1: types.Real):
        """
        Initializes ``Kz``.

        Parameters:
            z: On-z-axis cone center z component.
            t_squared: On-z-axis cone t^2 coefficent.
            plusminus_1: On-z-axis cone sheet selector.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, z)
        if t_squared is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, t_squared)
        if plusminus_1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, plusminus_1)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                z,
                t_squared,
                plusminus_1,
            ]
        )

        self.z: typing.Final[types.Real] = z
        self.t_squared: typing.Final[types.Real] = t_squared
        self.plusminus_1: typing.Final[types.Real] = plusminus_1

    def draw(self):
        """
        Generates ``Visualization`` from ``Kz``.

        Returns:
            ``pyvista.PolyData`` for ``Kz``.
        """

        vis = _visualization.Visualization.get_cone_quadratic(
            self.t_squared.value ** (1 / 2), self.plusminus_1.value
        )
        vis = vis.add_translation(_visualization.Vector(0, 0, self.z.value))

        return vis
