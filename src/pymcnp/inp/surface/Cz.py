import re

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Cz(_option.SurfaceOption):
    """
    Represents INP cz elements.

    Attributes:
        r: On-z-axis cylinder radius.
    """

    _KEYWORD = 'cz'

    _ATTRS = {
        'r': types.Real,
    }

    _REGEX = re.compile(rf'\Acz( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, r: str | int | float | types.Real):
        """
        Initializes ``Cz``.

        Parameters:
            r: On-z-axis cylinder radius.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.r: types.Real = r

    @property
    def r(self) -> types.Real:
        """
        Gets ``r``.

        Returns:
            ``r``.
        """

        return self._r

    @r.setter
    def r(self, r: str | int | float | types.Real) -> None:
        """
        Sets ``r``.

        Parameters:
            r: On-z-axis cylinder radius.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if r is not None:
            if isinstance(r, types.Real):
                r = r
            elif isinstance(r, int):
                r = types.Real(r)
            elif isinstance(r, float):
                r = types.Real(r)
            elif isinstance(r, str):
                r = types.Real.from_mcnp(r)
            else:
                raise TypeError

        if r is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, r)

        self._r: types.Real = r

    def draw(self):
        """
        Generates ``Visualization`` from ``Cz``.

        Returns:
            ``pyvista.PolyData`` for ``Cz``.
        """

        vis = _visualization.Visualization.get_cylinder_unbounded(float(self.r))

        return vis
