import re

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Pz(_option.SurfaceOption):
    """
    Represents INP pz elements.

    Attributes:
        d: Normal-to-the-z-axis plane D coefficent.
    """

    _KEYWORD = 'pz'

    _ATTRS = {
        'd': types.Real,
    }

    _REGEX = re.compile(rf'\Apz( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, d: str | int | float | types.Real):
        """
        Initializes ``Pz``.

        Parameters:
            d: Normal-to-the-z-axis plane D coefficent.

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
            d: Normal-to-the-z-axis plane D coefficent.

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
        Generates ``Visualization`` from ``Pz``.

        Returns:
            ``pyvista.PolyData`` for ``Pz``
        """

        vis = _visualization.Visualization.get_plane(0, 0, 1, float(self.d))

        return vis
