import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Ky(_option.SurfaceOption):
    """
    Represents INP ky elements.

    Attributes:
        y: On-y-axis cone center y component.
        t_squared: On-y-axis cone t^2 coefficent.
        plusminus_1: On-y-axis cone sheet selector.
    """

    _KEYWORD = 'ky'

    _ATTRS = {
        'y': types.Real,
        't_squared': types.Real,
        'plusminus_1': types.Real,
    }

    _REGEX = re.compile(rf'\Aky( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, y: types.Real, t_squared: types.Real, plusminus_1: types.Real):
        """
        Initializes ``Ky``.

        Parameters:
            y: On-y-axis cone center y component.
            t_squared: On-y-axis cone t^2 coefficent.
            plusminus_1: On-y-axis cone sheet selector.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y)
        if t_squared is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, t_squared)
        if plusminus_1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, plusminus_1)

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

        vis = _visualization.Visualization.get_cone_unbounded(self.t_squared.value ** (1 / 2), self.plusminus_1.value)
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(0, self.y.value, 0))

        return vis


@dataclasses.dataclass
class KyBuilder(_option.SurfaceOptionBuilder):
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

        y = self.y
        if isinstance(self.y, types.Real):
            y = self.y
        elif isinstance(self.y, float) or isinstance(self.y, int):
            y = types.Real(self.y)
        elif isinstance(self.y, str):
            y = types.Real.from_mcnp(self.y)

        t_squared = self.t_squared
        if isinstance(self.t_squared, types.Real):
            t_squared = self.t_squared
        elif isinstance(self.t_squared, float) or isinstance(self.t_squared, int):
            t_squared = types.Real(self.t_squared)
        elif isinstance(self.t_squared, str):
            t_squared = types.Real.from_mcnp(self.t_squared)

        plusminus_1 = self.plusminus_1
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

    @staticmethod
    def unbuild(ast: Ky):
        """
        Unbuilds ``Ky`` into ``KyBuilder``

        Returns:
            ``KyBuilder`` for ``Ky``.
        """

        return KyBuilder(
            y=copy.deepcopy(ast.y),
            t_squared=copy.deepcopy(ast.t_squared),
            plusminus_1=copy.deepcopy(ast.plusminus_1),
        )
