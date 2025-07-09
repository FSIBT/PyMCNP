import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Kx(_option.SurfaceOption):
    """
    Represents INP kx elements.

    Attributes:
        x: On-x-axis cone center x component.
        t_squared: On-x-axis cone t^2 coefficent.
        plusminus_1: On-x-axis cone sheet selector.
    """

    _KEYWORD = 'kx'

    _ATTRS = {
        'x': types.Real,
        't_squared': types.Real,
        'plusminus_1': types.Real,
    }

    _REGEX = re.compile(rf'\Akx( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, x: types.Real, t_squared: types.Real, plusminus_1: types.Real):
        """
        Initializes ``Kx``.

        Parameters:
            x: On-x-axis cone center x component.
            t_squared: On-x-axis cone t^2 coefficent.
            plusminus_1: On-x-axis cone sheet selector.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x)
        if t_squared is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, t_squared)
        if plusminus_1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, plusminus_1)

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

    def draw(self):
        """
        Generates ``Visualization`` from ``Kx``.

        Returns:
            ``pyvista.PolyData`` for ``Kx``.
        """

        vis = _visualization.Visualization.get_cone_unbounded(float(self.t_squared) ** (1 / 2), float(self.plusminus_1))
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x, 0, 0))

        return vis


@dataclasses.dataclass
class KxBuilder(_option.SurfaceOptionBuilder):
    """
    Builds ``Kx``.

    Attributes:
        x: On-x-axis cone center x component.
        t_squared: On-x-axis cone t^2 coefficent.
        plusminus_1: On-x-axis cone sheet selector.
    """

    x: str | float | types.Real
    t_squared: str | float | types.Real
    plusminus_1: str | float | types.Real

    def build(self):
        """
        Builds ``KxBuilder`` into ``Kx``.

        Returns:
            ``Kx`` for ``KxBuilder``.
        """

        x = self.x
        if isinstance(self.x, types.Real):
            x = self.x
        elif isinstance(self.x, float) or isinstance(self.x, int):
            x = types.Real(self.x)
        elif isinstance(self.x, str):
            x = types.Real.from_mcnp(self.x)

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

        return Kx(
            x=x,
            t_squared=t_squared,
            plusminus_1=plusminus_1,
        )

    @staticmethod
    def unbuild(ast: Kx):
        """
        Unbuilds ``Kx`` into ``KxBuilder``

        Returns:
            ``KxBuilder`` for ``Kx``.
        """

        return KxBuilder(
            x=copy.deepcopy(ast.x),
            t_squared=copy.deepcopy(ast.t_squared),
            plusminus_1=copy.deepcopy(ast.plusminus_1),
        )
