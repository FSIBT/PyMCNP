import re

import numpy

from . import _field
from . import _surface
from .. import _show
from .. import types
from .. import errors


class C_y(_surface.Surface):
    """
    Represents INP `c/y` surface cards.
    """

    _KEYWORD = 'c/y'

    x = _field.Field(types.Real, 'Parallel-to-y-axis cylinder center x component', required=True, code=errors.InpCode.SEMANTICS_OPTION)
    z = _field.Field(types.Real, 'Parallel-to-y-axis cylinder center z component', required=True, code=errors.InpCode.SEMANTICS_OPTION)
    r = _field.Field(types.Real, 'Parallel-to-y-axis cylinder radius', required=True, code=errors.InpCode.SEMANTICS_OPTION)

    _REGEX = re.compile(rf'\A(\+|\*)?(\S+)( \S+)? c/y( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `C_y`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `C_y`.
        """

        vis = shapes.CylinderUnbounded(float(self.r))
        vis = vis.rotate(numpy.array((1, 0, 0)), 90, (0, 0, 0))
        vis = vis.translate(numpy.array((float(self.x), 0, float(self.z))))

        return vis
