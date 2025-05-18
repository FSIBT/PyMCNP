import re
import typing
import dataclasses


from ._option import SurfaceOption
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class K_z(SurfaceOption):
    """
    Represents INP k/z elements.

    Attributes:
        x: Parallel-to-z-axis cone center x component.
        y: Parallel-to-z-axis cone center y component.
        z: Parallel-to-z-axis cone center z component.
        t_squared: Parallel-to-z-axis cone t^2 coefficent.
        plusminus_1: Parallel-to-z-axis cone sheet selector.
    """

    _ATTRS = {
        'x': types.Real,
        'y': types.Real,
        'z': types.Real,
        't_squared': types.Real,
        'plusminus_1': types.Real,
    }

    _REGEX = re.compile(
        rf'\Ak/z( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})\Z'
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
        Initializes ``K_z``.

        Parameters:
            x: Parallel-to-z-axis cone center x component.
            y: Parallel-to-z-axis cone center y component.
            z: Parallel-to-z-axis cone center z component.
            t_squared: Parallel-to-z-axis cone t^2 coefficent.
            plusminus_1: Parallel-to-z-axis cone sheet selector.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x)
        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y)
        if z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z)
        if t_squared is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, t_squared)
        if plusminus_1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, plusminus_1)

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
        Generates ``Visualization`` from ``K_z``.

        Returns:
            ``pyvista.PolyData`` for ``K_z``.
        """

        vis = _visualization.Visualization.get_cone_quadratic(
            self.t_squared.value ** (1 / 2), self.plusminus_1.value
        )
        vis = vis.add_translation(_visualization.Vector(self.x.value, self.y.value, self.z.value))

        return vis


@dataclasses.dataclass
class K_zBuilder:
    """
    Builds ``K_z``.

    Attributes:
        x: Parallel-to-z-axis cone center x component.
        y: Parallel-to-z-axis cone center y component.
        z: Parallel-to-z-axis cone center z component.
        t_squared: Parallel-to-z-axis cone t^2 coefficent.
        plusminus_1: Parallel-to-z-axis cone sheet selector.
    """

    x: str | float | types.Real
    y: str | float | types.Real
    z: str | float | types.Real
    t_squared: str | float | types.Real
    plusminus_1: str | float | types.Real

    def build(self):
        """
        Builds ``K_zBuilder`` into ``K_z``.

        Returns:
            ``K_z`` for ``K_zBuilder``.
        """

        x = self.x
        if isinstance(self.x, types.Real):
            x = self.x
        elif isinstance(self.x, float) or isinstance(self.x, int):
            x = types.Real(self.x)
        elif isinstance(self.x, str):
            x = types.Real.from_mcnp(self.x)

        y = self.y
        if isinstance(self.y, types.Real):
            y = self.y
        elif isinstance(self.y, float) or isinstance(self.y, int):
            y = types.Real(self.y)
        elif isinstance(self.y, str):
            y = types.Real.from_mcnp(self.y)

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

        return K_z(
            x=x,
            y=y,
            z=z,
            t_squared=t_squared,
            plusminus_1=plusminus_1,
        )
