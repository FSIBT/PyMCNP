import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Kx(SurfaceOption_, keyword='kx'):
    """
    Represents INP kx elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'x': types.Real,
        't_squared': types.Real,
        'plusminus_1': types.Real,
    }

    _REGEX = re.compile(
        rf'kx( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
    )

    def __init__(self, x: types.Real, t_squared: types.Real, plusminus_1: types.Real):
        """
        Initializes ``Kx``.

        Parameters:
            x: On-x-axis cone center x component.
            t_squared: On-x-axis cone t^2 coefficent.
            plusminus_1: On-x-axis cone sheet selector.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x)
        if t_squared is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, t_squared)
        if plusminus_1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, plusminus_1)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x,
                t_squared,
                plusminus_1,
            ]
        )

        self.x: typing.Final[types.Real] = x
        self.t_squared: typing.Final[types.Real] = t_squared
        self.plusminus_1: typing.Final[types.Real] = plusminus_1

        def to_pyvista(self):
            """
            Generates ``pyvista.PolyData`` from ``Kx``.

            Returns:
                ``pyvista.PolyData`` for ``Kx``.
            """

            vis = _visualization.McnpVisualization.get_cone_quadratic(
                self.t_squared.value ** (1 / 2), self.plusminus_1.value
            )
            vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))
            vis = vis.add_translation(_visualization.Vector(self.x.value, 0, 0))

            return vis.data
