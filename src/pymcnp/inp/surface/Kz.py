import re
import copy
import typing
import dataclasses


from ._option import SurfaceOption
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Kz(SurfaceOption):
    """
    Represents INP kz elements.

    Attributes:
        z: On-z-axis cone center z component.
        t_squared: On-z-axis cone t^2 coefficent.
        plusminus_1: On-z-axis cone sheet selector.
    """

    _KEYWORD = 'kz'

    _ATTRS = {
        'z': types.Real,
        't_squared': types.Real,
        'plusminus_1': types.Real,
    }

    _REGEX = re.compile(
        rf'\Akz( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z'
    )

    def __init__(self, z: types.Real, t_squared: types.Real, plusminus_1: types.Real):
        """
        Initializes ``Kz``.

        Parameters:
            z: On-z-axis cone center z component.
            t_squared: On-z-axis cone t^2 coefficent.
            plusminus_1: On-z-axis cone sheet selector.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z)
        if t_squared is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, t_squared)
        if plusminus_1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, plusminus_1)

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

        vis = _visualization.Visualization.get_cone_unbounded(
            self.t_squared.value ** (1 / 2), self.plusminus_1.value
        )
        vis = vis.add_translation(_visualization.Vector(0, 0, self.z.value))

        return vis


@dataclasses.dataclass
class KzBuilder:
    """
    Builds ``Kz``.

    Attributes:
        z: On-z-axis cone center z component.
        t_squared: On-z-axis cone t^2 coefficent.
        plusminus_1: On-z-axis cone sheet selector.
    """

    z: str | float | types.Real
    t_squared: str | float | types.Real
    plusminus_1: str | float | types.Real

    def build(self):
        """
        Builds ``KzBuilder`` into ``Kz``.

        Returns:
            ``Kz`` for ``KzBuilder``.
        """

        z = self.z
        if isinstance(self.z, types.Real):
            z = self.z
        elif isinstance(self.z, float) or isinstance(self.z, int):
            z = types.Real(self.z)
        elif isinstance(self.z, str):
            z = types.Real.from_mcnp(self.z)

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

        return Kz(
            z=z,
            t_squared=t_squared,
            plusminus_1=plusminus_1,
        )

    @staticmethod
    def unbuild(ast: Kz):
        """
        Unbuilds ``Kz`` into ``KzBuilder``

        Returns:
            ``KzBuilder`` for ``Kz``.
        """

        return Kz(
            z=copy.deepcopy(ast.z),
            t_squared=copy.deepcopy(ast.t_squared),
            plusminus_1=copy.deepcopy(ast.plusminus_1),
        )
