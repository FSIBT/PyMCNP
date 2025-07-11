import re

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Cx(_option.SurfaceOption):
    """
    Represents INP cx elements.

    Attributes:
        r: On-x-axis cylinder radius.
    """

    _KEYWORD = 'cx'

    _ATTRS = {
        'r': types.Real,
    }

    _REGEX = re.compile(rf'\Acx( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, r: str | int | float | types.Real):
        """
        Initializes ``Cx``.

        Parameters:
            r: On-x-axis cylinder radius.

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
            r: On-x-axis cylinder radius.

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
        Generates ``Visualization`` from ``Cx``.

        Returns:
            ``pyvista.PolyData`` for ``Cx``.
        """

        vis = _visualization.Visualization.get_cylinder_unbounded(float(self.r))
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))

        return vis
