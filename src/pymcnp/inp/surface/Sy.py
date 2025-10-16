import re

import numpy

from . import _option
from ... import _show
from ... import types
from ... import errors


class Sy(_option.SurfaceOption):
    """
    Represents INP `sy` elements.
    """

    _KEYWORD = 'sy'

    _ATTRS = {
        'y': types.Real,
        'r': types.Real,
    }

    _REGEX = re.compile(rf'\Asy( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, y: str | int | float | types.Real, r: str | int | float | types.Real):
        """
        Initializes `Sy`.

        Parameters:
            y: On-y-axis sphere center y component.
            r: On-y-axis sphere radius.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.y: types.Real = y
        self.r: types.Real = r

    @property
    def y(self) -> types.Real:
        """
        On-y-axis sphere center y component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._y

    @y.setter
    def y(self, y: str | int | float | types.Real) -> None:
        """
        Sets `y`.

        Parameters:
            y: On-y-axis sphere center y component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if y is not None:
            if isinstance(y, types.Real):
                y = y
            elif isinstance(y, int) or isinstance(y, float):
                y = types.Real(y)
            elif isinstance(y, str):
                y = types.Real.from_mcnp(y)

        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y)

        self._y: types.Real = y

    @property
    def r(self) -> types.Real:
        """
        On-y-axis sphere radius

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._r

    @r.setter
    def r(self, r: str | int | float | types.Real) -> None:
        """
        Sets `r`.

        Parameters:
            r: On-y-axis sphere radius.

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

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Sy`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Sy`
        """

        vis = shapes.Sphere(float(self.r))
        vis = vis.rotate(numpy.array((1, 0, 0)), 90, (0, 0, 0))
        vis = vis.translate(numpy.array((0, float(self.y), 0)))

        return vis
