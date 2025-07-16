import re

from . import _option
from ... import types
from ... import errors
from ...utils import _visualization


class Cy(_option.SurfaceOption):
    """
    Represents INP cy elements.
    """

    _KEYWORD = 'cy'

    _ATTRS = {
        'r': types.Real,
    }

    _REGEX = re.compile(rf'\Acy( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, r: str | int | float | types.Real):
        """
        Initializes ``Cy``.

        Parameters:
            r: On-y-axis cylinder radius.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.r: types.Real = r

    @property
    def r(self) -> types.Real:
        """
        On-y-axis cylinder radius

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._r

    @r.setter
    def r(self, r: str | int | float | types.Real) -> None:
        """
        Sets ``r``.

        Parameters:
            r: On-y-axis cylinder radius.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if r is not None:
            if isinstance(r, types.Real):
                r = r
            elif isinstance(r, int) or isinstance(r, float):
                r = types.Real(r)
            elif isinstance(r, str):
                r = types.Real.from_mcnp(r)

        if r is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, r)

        self._r: types.Real = r

    def draw(self):
        """
        Generates ``Visualization`` from ``Cy``.

        Returns:
            ``pyvista.PolyData`` for ``Cy``.
        """

        vis = _visualization.Visualization.get_cylinder_unbounded(float(self.r))
        vis = vis.add_rotation(_visualization.Vector(1, 0, 0), 90, (0, 0, 0))

        return vis
