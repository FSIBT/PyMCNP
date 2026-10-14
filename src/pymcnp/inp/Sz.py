import re

import numpy

from . import _field
from . import _surface
from .. import _show
from .. import types
from .. import errors


class Sz(_surface.Surface):
    """
    Represents INP `sz` surface cards.
    """

    _KEYWORD = 'sz'

    z = _field.Field(types.Real, 'On-z-axis sphere center z component', required=True, code=errors.InpCode.SEMANTICS_OPTION)
    r = _field.Field(types.Real, 'On-z-axis sphere radius', required=True, code=errors.InpCode.SEMANTICS_OPTION)

    _REGEX = re.compile(rf'\A(\+|\*)?(\S+)( \S+)? sz( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Sz`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Sz`
        """

        vis = shapes.Sphere(float(self.r))
        vis = vis.translate(numpy.array((0, 0, float(self.z))))

        return vis
