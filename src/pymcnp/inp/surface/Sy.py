import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Sy(SurfaceOption_, keyword='sy'):
    """
    Represents INP sy elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'y': types.Real,
        'r': types.Real,
    }

    _REGEX = re.compile(rf'\Asy( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})\Z')

    def __init__(self, y: types.Real, r: types.Real):
        """
        Initializes ``Sy``.

        Parameters:
            y: On-y-axis sphere center y component.
            r: On-y-axis sphere radius.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, y)
        if r is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, r)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                y,
                r,
            ]
        )

        self.y: typing.Final[types.Real] = y
        self.r: typing.Final[types.Real] = r

    def draw(self):
        """
        Generates ``Visualization`` from ``Sy``.

        Returns:
            ``pyvista.PolyData`` for ``Sy``
        """

        vis = _visualization.Visualization.get_sphere(self.r.value)
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(0, self.y.value, 0))

        return vis
