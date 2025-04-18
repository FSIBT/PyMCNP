import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class So(SurfaceOption_, keyword='so'):
    """
    Represents INP so elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'r': types.Real,
    }

    _REGEX = re.compile(rf'\Aso( {types.Real._REGEX.pattern})\Z')

    def __init__(self, r: types.Real):
        """
        Initializes ``So``.

        Parameters:
            r: Origin-centered sphere radius.

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
        Generates ``Visualization`` from ``So``.

        Returns:
            ``pyvista.PolyData`` for ``So``
        """

        vis = _visualization.Visualization.get_sphere(self.r.value)

        return vis
