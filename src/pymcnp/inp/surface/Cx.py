import re

import numpy

from . import _option
from ... import _show
from ... import types
from ... import errors


class Cx(_option.SurfaceOption):
    """
    Represents INP `cx` elements.
    """

    _KEYWORD = 'cx'

    _ATTRS = {
        'r': types.Real,
    }

    _REGEX = re.compile(rf'\Acx( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, r: str | int | float | types.Real):
        """
        Initializes `Cx`.

        Parameters:
            r: On-x-axis cylinder radius.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.r: types.Real = r

    @property
    def r(self) -> types.Real:
        """
        On-x-axis cylinder radius

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
            r: On-x-axis cylinder radius.

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
        Generates `Visualization` from `Cx`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Cx`.
        """

        vis = shapes.CylinderUnbounded(float(self.r))
        vis = vis.rotate(numpy.array((0, 1, 0)), 90, (0, 0, 0))

        return vis
