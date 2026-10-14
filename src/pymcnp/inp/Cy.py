import re

import numpy

from . import _field
from . import _surface
from .. import _show
from .. import types
from .. import errors


class Cy(_surface.Surface):
    """
    Represents INP `cy` surface cards.
    """

    _KEYWORD = 'cy'

    r = _field.Field(types.Real, 'On-y-axis cylinder radius', required=True, code=errors.InpCode.SEMANTICS_OPTION)

    _REGEX = re.compile(rf'\A(\+|\*)?(\S+)( \S+)? cy( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Cy`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Cy`.
        """

        vis = shapes.CylinderUnbounded(float(self.r))
        vis = vis.rotate(numpy.array((1, 0, 0)), 90, (0, 0, 0))

        return vis
