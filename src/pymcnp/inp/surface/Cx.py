import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Cx(SurfaceOption_, keyword='cx'):
    """
    Represents INP cx elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'r': types.Real,
    }

    _REGEX = re.compile(rf'cx( {types.Real._REGEX.pattern})')

    def __init__(self, r: types.Real):
        """
        Initializes ``Cx``.

        Parameters:
            r: On-x-axis cylinder radius.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if r is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, r)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                r,
            ]
        )

        self.r: typing.Final[types.Real] = r

    def draw(self):
        """
        Generates ``Visualization`` from ``Cx``.

        Returns:
            ``pyvista.PolyData`` for ``Cx``.
        """

        vis = _visualization.Visualization.get_cylinder_unbounded(self.r.value)
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))

        return vis
