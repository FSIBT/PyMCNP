import re

import numpy

from . import _field
from . import _surface
from .. import _show
from .. import types
from .. import errors


class C_x(_surface.Surface):
    """
    Represents INP `c/x` surface cards.
    """

    _KEYWORD = 'c/x'

    y = _field.Field(types.Real, 'Parallel-to-x-axis cylinder center y component', required=True, code=errors.InpCode.SEMANTICS_OPTION)
    z = _field.Field(types.Real, 'Parallel-to-x-axis cylinder center z component', required=True, code=errors.InpCode.SEMANTICS_OPTION)
    r = _field.Field(types.Real, 'Parallel-to-x-axis cylinder radius', required=True, code=errors.InpCode.SEMANTICS_OPTION)

    _REGEX = re.compile(rf'\A(\+|\*)?(\S+)( \S+)? c/x( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `C_x`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `C_x`.
        """

        vis = shapes.CylinderUnbounded(float(self.r))
        vis = vis.rotate(numpy.array((0, 1, 0)), 90, (0, 0, 0))
        vis = vis.translate(numpy.array((0, float(self.y), float(self.z))))

        return vis
