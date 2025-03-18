import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class P_1(SurfaceOption_, keyword='p'):
    """
    Represents INP p_1 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
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
        rf'p( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
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
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if x1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x1)
        if y1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, y1)
        if z1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, z1)
        if x2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x2)
        if y2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, y2)
        if z2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, z2)
        if x3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x3)
        if y3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, y3)
        if z3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, z3)

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
