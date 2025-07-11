import re

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Sx(_option.SurfaceOption):
    """
    Represents INP sx elements.

    Attributes:
        x: On-x-axis sphere center x component.
        r: On-x-axis sphere radius.
    """

    _KEYWORD = 'sx'

    _ATTRS = {
        'x': types.Real,
        'r': types.Real,
    }

    _REGEX = re.compile(rf'\Asx( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, x: str | int | float | types.Real, r: str | int | float | types.Real):
        """
        Initializes ``Sx``.

        Parameters:
            x: On-x-axis sphere center x component.
            r: On-x-axis sphere radius.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.x: types.Real = x
        self.r: types.Real = r

    @property
    def x(self) -> types.Real:
        """
        Gets ``x``.

        Returns:
            ``x``.
        """

        return self._x

    @x.setter
    def x(self, x: str | int | float | types.Real) -> None:
        """
        Sets ``x``.

        Parameters:
            x: On-x-axis sphere center x component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if x is not None:
            if isinstance(x, types.Real):
                x = x
            elif isinstance(x, int):
                x = types.Real(x)
            elif isinstance(x, float):
                x = types.Real(x)
            elif isinstance(x, str):
                x = types.Real.from_mcnp(x)
            else:
                raise TypeError

        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x)

        self._x: types.Real = x

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
            r: On-x-axis sphere radius.

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
        Generates ``Visualization`` from ``Sx``.

        Returns:
            ``pyvista.PolyData`` for ``Sx``
        """

        vis = _visualization.Visualization.get_sphere(float(self.r))
        vis = vis.add_translation(_visualization.Vector(self.x, 0, 0))

        return vis
