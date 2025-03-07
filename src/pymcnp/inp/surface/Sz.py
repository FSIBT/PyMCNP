import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Sz(SurfaceOption_, keyword='sz'):
    """
    Represents INP sz elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'z': types.Real,
        'r': types.Real,
    }

    _REGEX = re.compile(rf'sz( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})')

    def __init__(self, z: types.Real, r: types.Real):
        """
        Initializes ``Sz``.

        Parameters:
            z: On-z-axis sphere center z component.
            r: On-z-axis sphere radius.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, z)
        if r is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, r)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                z,
                r,
            ]
        )

        self.z: typing.Final[types.Real] = z
        self.r: typing.Final[types.Real] = r

        def to_pyvista(self):
            """
            Generates ``pyvista.PolyData`` from ``Sz``.

            Returns:
                ``pyvista.PolyData`` for ``Sz``
            """

            vis = _visualization.McnpVisualization.get_sphere(self.r.value)
            vis = vis.add_translation(_visualization.Vector(0, 0, self.z.value))

            return vis.data
