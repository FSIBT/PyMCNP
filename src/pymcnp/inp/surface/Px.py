import re

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Px(_option.SurfaceOption):
    """
    Represents INP px elements.
    """

    _KEYWORD = 'px'

    _ATTRS = {
        'd': types.Real,
    }

    _REGEX = re.compile(rf'\Apx( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, d: str | int | float | types.Real):
        """
        Initializes ``Px``.

        Parameters:
            d: Normal-to-the-x-axis plane D coefficent.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.d: types.Real = d

    @property
    def d(self) -> types.Real:
        """
        Normal-to-the-x-axis plane D coefficent

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._d

    @d.setter
    def d(self, d: str | int | float | types.Real) -> None:
        """
        Sets ``d``.

        Parameters:
            d: Normal-to-the-x-axis plane D coefficent.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if d is not None:
            if isinstance(d, types.Real):
                d = d
            elif isinstance(d, int) or isinstance(d, float):
                d = types.Real(d)
            elif isinstance(d, str):
                d = types.Real.from_mcnp(d)

        if d is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, d)

        self._d: types.Real = d

    def draw(self):
        """
        Generates ``Visualization`` from ``Px``.

        Returns:
            ``pyvista.PolyData`` for ``Px``
        """

        vis = _visualization.Visualization.get_plane(1, 0, 0, float(self.d))
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))

        return vis
