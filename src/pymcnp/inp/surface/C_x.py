import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class C_x(SurfaceOption_, keyword='c/x'):
    """
    Represents INP c/x elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'y': types.Real,
        'z': types.Real,
        'r': types.Real,
    }

    _REGEX = re.compile(
        rf'\Ac/x( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})\Z'
    )

    def __init__(self, y: types.Real, z: types.Real, r: types.Real):
        """
        Initializes ``C_x``.

        Parameters:
            y: Parallel-to-x-axis cylinder center y component.
            z: Parallel-to-x-axis cylinder center z component.
            r: Parallel-to-x-axis cylinder radius.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, y)
        if z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, z)
        if r is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, r)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                y,
                z,
                r,
            ]
        )

        self.y: typing.Final[types.Real] = y
        self.z: typing.Final[types.Real] = z
        self.r: typing.Final[types.Real] = r

    def draw(self):
        """
        Generates ``Visualization`` from ``C_x``.

        Returns:
            ``pyvista.PolyData`` for ``C_x``.
        """

        vis = _visualization.Visualization.get_cylinder_unbounded(self.r.value)
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(0, self.y.value, self.z.value))

        return vis
