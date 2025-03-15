import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Px(SurfaceOption_, keyword='px'):
    """
    Represents INP px elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'd': types.Real,
    }

    _REGEX = re.compile(rf'px( {types.Real._REGEX.pattern})')

    def __init__(self, d: types.Real):
        """
        Initializes ``Px``.

        Parameters:
            d: Normal-to-the-x-axis plane D coefficent.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if d is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, d)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                d,
            ]
        )

        self.d: typing.Final[types.Real] = d

    def to_pyvista(self):
        """
        Generates ``pyvista.PolyData`` from ``Px``.

        Returns:
            ``pyvista.PolyData`` for ``Px``
        """

        vis = _visualization.McnpVisualization.get_plane(1, 0, 0, self.d.value)
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))

        return vis
