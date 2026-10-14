import re

import numpy

from . import _field
from . import _surface
from .. import _show
from .. import types
from .. import errors


class Sx(_surface.Surface):
    """
    Represents INP `sx` surface cards.
    """

    _KEYWORD = 'sx'

    x = _field.Field(types.Real, 'On-x-axis sphere center x component', required=True, code=errors.InpCode.SEMANTICS_OPTION)
    r = _field.Field(types.Real, 'On-x-axis sphere radius', required=True, code=errors.InpCode.SEMANTICS_OPTION)

    _REGEX = re.compile(rf'\A(\+|\*)?(\S+)( \S+)? sx( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Sx`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Sx`
        """

        vis = shapes.Sphere(float(self.r))
        vis = vis.translate(numpy.array((float(self.x), 0, 0)))

        return vis
