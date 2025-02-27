import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Sx(SurfaceOption_, keyword='sx'):
    """
    Represents INP sx elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'x': types.Real,
        'r': types.Real,
    }

    _REGEX = re.compile(r'sx( \S+)( \S+)')

    def __init__(self, x: types.Real, r: types.Real):
        """
        Initializes ``Sx``.

        Parameters:
            x: On-x-axis sphere center x component.
            r: On-x-axis sphere radius.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x)
        if r is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, r)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x,
                r,
            ]
        )

        self.x: typing.Final[types.Real] = x
        self.r: typing.Final[types.Real] = r

        def to_pyvista(self):
            """
            Generates ``pyvista.PolyData`` from ``Sx``.

            Returns:
                ``pyvista.PolyData`` for ``Sx``
            """

            vis = _visualization.McnpVisualization.get_sphere(self.r.value)
            vis = vis.add_translation(_visualization.Vector(self.x.value, 0, 0))

            return vis.data
