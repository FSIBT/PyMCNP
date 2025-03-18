import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class S(SurfaceOption_, keyword='s'):
    """
    Represents INP s elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'x': types.Real,
        'y': types.Real,
        'z': types.Real,
        'r': types.Real,
    }

    _REGEX = re.compile(
        rf's( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
    )

    def __init__(self, x: types.Real, y: types.Real, z: types.Real, r: types.Real):
        """
        Initializes ``S``.

        Parameters:
            x: General sphere center x component.
            y: General sphere center y component.
            z: General sphere center z component.
            r: General sphere radius.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x)
        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, y)
        if z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, z)
        if r is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, r)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x,
                y,
                z,
                r,
            ]
        )

        self.x: typing.Final[types.Real] = x
        self.y: typing.Final[types.Real] = y
        self.z: typing.Final[types.Real] = z
        self.r: typing.Final[types.Real] = r

    def draw(self):
        """
        Generates ``Visualization`` from ``S``.

        Returns:
            ``pyvista.PolyData`` for ``S``
        """

        vis = _visualization.Visualization.get_sphere(self.r.value)
        vis = vis.add_translation(_visualization.Vector(self.x.value, self.y.value, self.z.value))

        return vis
