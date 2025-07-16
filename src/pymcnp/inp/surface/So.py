import re

from . import _option
from ... import types
from ... import errors
from ...utils import _visualization


class So(_option.SurfaceOption):
    """
    Represents INP so elements.
    """

    _KEYWORD = 'so'

    _ATTRS = {
        'r': types.Real,
    }

    _REGEX = re.compile(rf'\Aso( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, r: str | int | float | types.Real):
        """
        Initializes ``So``.

        Parameters:
            r: Origin-centered sphere radius.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.r: types.Real = r

    @property
    def r(self) -> types.Real:
        """
        Origin-centered sphere radius

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
            r: Origin-centered sphere radius.

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
        Generates ``Visualization`` from ``So``.

        Returns:
            ``pyvista.PolyData`` for ``So``
        """

        vis = _visualization.Visualization.get_sphere(float(self.r))

        return vis
