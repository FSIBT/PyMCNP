import re

import numpy

from . import _field
from . import _surface
from .. import _show
from .. import types
from .. import errors


class S(_surface.Surface):
    """
    Represents INP `s` surface cards.
    """

    _KEYWORD = 's'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    x = _field.Field(types.Real, 'General sphere center x component', required=True)
    y = _field.Field(types.Real, 'General sphere center y component', required=True)
    z = _field.Field(types.Real, 'General sphere center z component', required=True)
    r = _field.Field(types.Real, 'General sphere radius', required=True)

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? s( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE
    )

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `S`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `S`
        """

        vis = shapes.Sphere(float(self.r))
        vis = vis.translate(numpy.array((float(self.x), float(self.y), float(self.z))))

        return vis
