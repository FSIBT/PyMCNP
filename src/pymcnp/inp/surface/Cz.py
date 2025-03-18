import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Cz(SurfaceOption_, keyword='cz'):
    """
    Represents INP cz elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'r': types.Real,
    }

    _REGEX = re.compile(rf'cz( {types.Real._REGEX.pattern})')

    def __init__(self, r: types.Real):
        """
        Initializes ``Cz``.

        Parameters:
            r: On-z-axis cylinder radius.

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
        Generates ``Visualization`` from ``Cz``.

        Returns:
            ``pyvista.PolyData`` for ``Cz``.
        """

        vis = _visualization.Visualization.get_cylinder_unbounded(self.r.value)

        return vis
