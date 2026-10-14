import re

import numpy

from . import _field
from . import _surface
from .. import _show
from .. import types
from .. import errors


class C_z(_surface.Surface):
    """
    Represents INP `c/z` surface cards.
    """

    _KEYWORD = 'c/z'

    x = _field.Field(types.Real, 'Parallel-to-z-axis cylinder center x component', required=True, code=errors.InpCode.SEMANTICS_OPTION)
    y = _field.Field(types.Real, 'Parallel-to-z-axis cylinder center y component', required=True, code=errors.InpCode.SEMANTICS_OPTION)
    r = _field.Field(types.Real, 'Parallel-to-z-axis cylinder radius', required=True, code=errors.InpCode.SEMANTICS_OPTION)

    _REGEX = re.compile(rf'\A(\+|\*)?(\S+)( \S+)? c/z( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `C_z`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `C_z`.
        """

        vis = shapes.CylinderUnbounded(float(self.r))
        vis = vis.rotate(numpy.array((0, 1, 0)), 90, (0, 0, 0))
        vis = vis.translate(numpy.array((float(self.x), float(self.y), 0)))

        return vis
