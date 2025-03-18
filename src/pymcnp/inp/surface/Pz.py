import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Pz(SurfaceOption_, keyword='pz'):
    """
    Represents INP pz elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'd': types.Real,
    }

    _REGEX = re.compile(rf'pz( {types.Real._REGEX.pattern})')

    def __init__(self, d: types.Real):
        """
        Initializes ``Pz``.

        Parameters:
            d: Normal-to-the-z-axis plane D coefficent.

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

    def draw(self):
        """
        Generates ``Visualization`` from ``Pz``.

        Returns:
            ``pyvista.PolyData`` for ``Pz``
        """

        vis = _visualization.Visualization.get_plane(0, 0, 1, self.d.value)

        return vis
