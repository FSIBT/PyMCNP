import re

import numpy

from . import _field
from . import _surface
from .. import _show
from .. import types
from .. import errors


class Sy(_surface.Surface):
    """
    Represents INP `sy` surface cards.
    """

    _KEYWORD = 'sy'

    y = _field.Field(types.Real, 'On-y-axis sphere center y component', required=True, code=errors.InpCode.SEMANTICS_OPTION)
    r = _field.Field(types.Real, 'On-y-axis sphere radius', required=True, code=errors.InpCode.SEMANTICS_OPTION)

    _REGEX = re.compile(rf'\A(\+|\*)?(\S+)( \S+)? sy( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

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
