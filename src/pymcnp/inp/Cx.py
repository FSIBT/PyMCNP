import re

import numpy

from . import _field
from . import _surface
from .. import _show
from .. import types
from .. import errors


class Cx(_surface.Surface):
    """
    Represents INP `cx` surface cards.
    """

    _KEYWORD = 'cx'

    r = _field.Field(types.Real, 'On-x-axis cylinder radius', required=True, code=errors.InpCode.SEMANTICS_OPTION)

    _REGEX = re.compile(rf'\A(\+|\*)?(\S+)( \S+)? cx( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

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
