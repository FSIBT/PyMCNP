import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class C_z(SurfaceOption_, keyword='c/z'):
    """
    Represents INP c/z elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'x': types.Real,
        'y': types.Real,
        'r': types.Real,
    }

    _REGEX = re.compile(
        rf'c/z( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
    )

    def __init__(self, x: types.Real, y: types.Real, r: types.Real):
        """
        Initializes ``C_z``.

        Parameters:
            x: Parallel-to-z-axis cylinder center x component.
            y: Parallel-to-z-axis cylinder center y component.
            r: Parallel-to-z-axis cylinder radius.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x)
        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, y)
        if r is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, r)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x,
                y,
                r,
            ]
        )

        self.x: typing.Final[types.Real] = x
        self.y: typing.Final[types.Real] = y
        self.r: typing.Final[types.Real] = r

    def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``C_z``.
        Returns:
            ``pyvista.PolyData`` for ``C_z``.
        """

        vis = _visualization.McnpVisualization.get_cylinder_unbounded(self.r.value)
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x.value, self.y.value, 0))

        return vis
