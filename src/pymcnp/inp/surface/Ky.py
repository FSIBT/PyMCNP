import re
import typing
import dataclasses


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Ky(SurfaceOption_, keyword='ky'):
    """
    Represents INP ky elements.

    Attributes:
        y: On-y-axis cone center y component.
        t_squared: On-y-axis cone t^2 coefficent.
        plusminus_1: On-y-axis cone sheet selector.
    """

    _ATTRS = {
        'y': types.Real,
        't_squared': types.Real,
        'plusminus_1': types.Real,
    }

    _REGEX = re.compile(
        rf'\Aky( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})\Z'
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


@dataclasses.dataclass
class KyBuilder:
    """
    Builds ``Ky``.

    Attributes:
        y: On-y-axis cone center y component.
        t_squared: On-y-axis cone t^2 coefficent.
        plusminus_1: On-y-axis cone sheet selector.
    """

    y: str | float | types.Real
    t_squared: str | float | types.Real
    plusminus_1: str | float | types.Real

    def build(self):
        """
        Builds ``KyBuilder`` into ``Ky``.

        Returns:
            ``Ky`` for ``KyBuilder``.
        """

        if isinstance(self.y, types.Real):
            y = self.y
        elif isinstance(self.y, float) or isinstance(self.y, int):
            y = types.Real(self.y)
        elif isinstance(self.y, str):
            y = types.Real.from_mcnp(self.y)

        if isinstance(self.t_squared, types.Real):
            t_squared = self.t_squared
        elif isinstance(self.t_squared, float) or isinstance(self.t_squared, int):
            t_squared = types.Real(self.t_squared)
        elif isinstance(self.t_squared, str):
            t_squared = types.Real.from_mcnp(self.t_squared)

        if isinstance(self.plusminus_1, types.Real):
            plusminus_1 = self.plusminus_1
        elif isinstance(self.plusminus_1, float) or isinstance(self.plusminus_1, int):
            plusminus_1 = types.Real(self.plusminus_1)
        elif isinstance(self.plusminus_1, str):
            plusminus_1 = types.Real.from_mcnp(self.plusminus_1)

        return Ky(
            y=y,
            t_squared=t_squared,
            plusminus_1=plusminus_1,
        )
