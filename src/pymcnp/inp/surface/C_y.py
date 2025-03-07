import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class C_y(SurfaceOption_, keyword='c/y'):
    """
    Represents INP c/y elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'x': types.Real,
        'z': types.Real,
        'r': types.Real,
    }

    _REGEX = re.compile(
        rf'c/y( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
    )

    def __init__(self, x: types.Real, z: types.Real, r: types.Real):
        """
        Initializes ``C_y``.

        Parameters:
            x: Parallel-to-y-axis cylinder center x component.
            z: Parallel-to-y-axis cylinder center z component.
            r: Parallel-to-y-axis cylinder radius.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x)
        if z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, z)
        if r is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, r)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x,
                z,
                r,
            ]
        )

        self.x: typing.Final[types.Real] = x
        self.z: typing.Final[types.Real] = z
        self.r: typing.Final[types.Real] = r

    def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``C_y``.

        Returns:
            ``pyvista.PolyData`` for ``C_y``.
        """

        vis = _visualization.McnpVisualization.get_cylinder_unbounded(self.r.value)
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x.value, 0, self.z.value))

        return vis.data
