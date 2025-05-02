import re
import typing
import dataclasses


from ._option import SurfaceOption
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class P_1(SurfaceOption):
    """
    Represents INP p variation #1 elements.

    Attributes:
        x1: point-defined general plane x-coordinate #1.
        y1: point-defined general plane y-coordinate #1.
        z1: point-defined general plane z-coordinate #1.
        x2: point-defined general plane x-coordinate #2.
        y2: point-defined general plane y-coordinate #2.
        z2: point-defined general plane z-coordinate #2.
        x3: point-defined general plane x-coordinate #3.
        y3: point-defined general plane y-coordinate #3.
        z3: point-defined general plane z-coordinate #3.
    """

    _ATTRS = {
        'x1': types.Real,
        'y1': types.Real,
        'z1': types.Real,
        'x2': types.Real,
        'y2': types.Real,
        'z2': types.Real,
        'x3': types.Real,
        'y3': types.Real,
        'z3': types.Real,
    }

    _REGEX = re.compile(
        rf'\Ap( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        x1: types.Real,
        y1: types.Real,
        z1: types.Real,
        x2: types.Real,
        y2: types.Real,
        z2: types.Real,
        x3: types.Real,
        y3: types.Real,
        z3: types.Real,
    ):
        """
        Initializes ``P_1``.

        Parameters:
            x1: point-defined general plane x-coordinate #1.
            y1: point-defined general plane y-coordinate #1.
            z1: point-defined general plane z-coordinate #1.
            x2: point-defined general plane x-coordinate #2.
            y2: point-defined general plane y-coordinate #2.
            z2: point-defined general plane z-coordinate #2.
            x3: point-defined general plane x-coordinate #3.
            y3: point-defined general plane y-coordinate #3.
            z3: point-defined general plane z-coordinate #3.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if x1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x1)
        if y1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y1)
        if z1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z1)
        if x2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x2)
        if y2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y2)
        if z2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z2)
        if x3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x3)
        if y3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y3)
        if z3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z3)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x1,
                y1,
                z1,
                x2,
                y2,
                z2,
                x3,
                y3,
                z3,
            ]
        )

        self.x1: typing.Final[types.Real] = x1
        self.y1: typing.Final[types.Real] = y1
        self.z1: typing.Final[types.Real] = z1
        self.x2: typing.Final[types.Real] = x2
        self.y2: typing.Final[types.Real] = y2
        self.z2: typing.Final[types.Real] = z2
        self.x3: typing.Final[types.Real] = x3
        self.y3: typing.Final[types.Real] = y3
        self.z3: typing.Final[types.Real] = z3

    def draw(self):
        """
        Generates ``Visualization`` from ``P0``.

        Returns:
            ``pyvista.PolyData`` for ``P1``
        """

        a = _visualization.Vector(self.x2 - self.x1, self.y2 - self.y1, self.z2 - self.z1)
        b = _visualization.Vector(self.x3 - self.x1, self.y3 - self.y1, self.z3 - self.z1)
        n = a * b

        vis = _visualization.Visualization.get_plane(
            n.x, n.y, n.z, n.x * self.x1 + n.y * self.y1 + n.z * self.z1
        )

        return vis


@dataclasses.dataclass
class PBuilder_1:
    """
    Builds ``P_1``.

    Attributes:
        x1: point-defined general plane x-coordinate #1.
        y1: point-defined general plane y-coordinate #1.
        z1: point-defined general plane z-coordinate #1.
        x2: point-defined general plane x-coordinate #2.
        y2: point-defined general plane y-coordinate #2.
        z2: point-defined general plane z-coordinate #2.
        x3: point-defined general plane x-coordinate #3.
        y3: point-defined general plane y-coordinate #3.
        z3: point-defined general plane z-coordinate #3.
    """

    x1: str | float | types.Real
    y1: str | float | types.Real
    z1: str | float | types.Real
    x2: str | float | types.Real
    y2: str | float | types.Real
    z2: str | float | types.Real
    x3: str | float | types.Real
    y3: str | float | types.Real
    z3: str | float | types.Real

    def build(self):
        """
        Builds ``PBuilder_1`` into ``P_1``.

        Returns:
            ``P_1`` for ``PBuilder_1``.
        """

        if isinstance(self.x1, types.Real):
            x1 = self.x1
        elif isinstance(self.x1, float) or isinstance(self.x1, int):
            x1 = types.Real(self.x1)
        elif isinstance(self.x1, str):
            x1 = types.Real.from_mcnp(self.x1)

        if isinstance(self.y1, types.Real):
            y1 = self.y1
        elif isinstance(self.y1, float) or isinstance(self.y1, int):
            y1 = types.Real(self.y1)
        elif isinstance(self.y1, str):
            y1 = types.Real.from_mcnp(self.y1)

        if isinstance(self.z1, types.Real):
            z1 = self.z1
        elif isinstance(self.z1, float) or isinstance(self.z1, int):
            z1 = types.Real(self.z1)
        elif isinstance(self.z1, str):
            z1 = types.Real.from_mcnp(self.z1)

        if isinstance(self.x2, types.Real):
            x2 = self.x2
        elif isinstance(self.x2, float) or isinstance(self.x2, int):
            x2 = types.Real(self.x2)
        elif isinstance(self.x2, str):
            x2 = types.Real.from_mcnp(self.x2)

        if isinstance(self.y2, types.Real):
            y2 = self.y2
        elif isinstance(self.y2, float) or isinstance(self.y2, int):
            y2 = types.Real(self.y2)
        elif isinstance(self.y2, str):
            y2 = types.Real.from_mcnp(self.y2)

        if isinstance(self.z2, types.Real):
            z2 = self.z2
        elif isinstance(self.z2, float) or isinstance(self.z2, int):
            z2 = types.Real(self.z2)
        elif isinstance(self.z2, str):
            z2 = types.Real.from_mcnp(self.z2)

        if isinstance(self.x3, types.Real):
            x3 = self.x3
        elif isinstance(self.x3, float) or isinstance(self.x3, int):
            x3 = types.Real(self.x3)
        elif isinstance(self.x3, str):
            x3 = types.Real.from_mcnp(self.x3)

        if isinstance(self.y3, types.Real):
            y3 = self.y3
        elif isinstance(self.y3, float) or isinstance(self.y3, int):
            y3 = types.Real(self.y3)
        elif isinstance(self.y3, str):
            y3 = types.Real.from_mcnp(self.y3)

        if isinstance(self.z3, types.Real):
            z3 = self.z3
        elif isinstance(self.z3, float) or isinstance(self.z3, int):
            z3 = types.Real(self.z3)
        elif isinstance(self.z3, str):
            z3 = types.Real.from_mcnp(self.z3)

        return P_1(
            x1=x1,
            y1=y1,
            z1=z1,
            x2=x2,
            y2=y2,
            z2=z2,
            x3=x3,
            y3=y3,
            z3=z3,
        )
