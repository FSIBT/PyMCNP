import re

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Py(_option.SurfaceOption):
    """
    Represents INP py elements.

    Attributes:
        d: Normal-to-the-y-axis plane D coefficent.
    """

    _KEYWORD = 'py'

    _ATTRS = {
        'd': types.Real,
    }

    _REGEX = re.compile(rf'\Apy( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, d: str | int | float | types.Real):
        """
        Initializes ``Py``.

        Parameters:
            d: Normal-to-the-y-axis plane D coefficent.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.d: types.Real = d

    @property
    def d(self) -> types.Real:
        """
        Gets ``d``.

        Returns:
            ``d``.
        """

        return self._d

    @d.setter
    def d(self, d: str | int | float | types.Real) -> None:
        """
        Sets ``d``.

        Parameters:
            d: Normal-to-the-y-axis plane D coefficent.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if d is not None:
            if isinstance(d, types.Real):
                d = d
            elif isinstance(d, int):
                d = types.Real(d)
            elif isinstance(d, float):
                d = types.Real(d)
            elif isinstance(d, str):
                d = types.Real.from_mcnp(d)
            else:
                raise TypeError

        if d is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, d)

        self._d: types.Real = d

    def draw(self):
        """
        Generates ``Visualization`` from ``Py``.

        Returns:
            ``pyvista.PolyData`` for ``Py``
        """

        vis = _visualization.Visualization.get_plane(0, 1, 0, float(self.d))
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))

        return vis
