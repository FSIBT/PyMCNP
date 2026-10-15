import re

import numpy

from . import _field
from . import _surface
from .. import _show
from .. import types
from .. import errors


class Tz(_surface.Surface):
    """
    Represents INP `tz` surface cards.
    """

    _KEYWORD = 'tz'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    x = _field.Field(types.Real, 'Parallel-to-z-axis tori center x component', required=True)
    y = _field.Field(types.Real, 'Parallel-to-z-axis tori center y component', required=True)
    z = _field.Field(types.Real, 'Parallel-to-z-axis tori center z component', required=True)
    a = _field.Field(types.Real, 'Parallel-to-z-axis tori A coefficent', required=True)
    b = _field.Field(types.Real, 'Parallel-to-z-axis tori B coefficent', required=True)
    c = _field.Field(types.Real, 'Parallel-to-z-axis tori C coefficent', required=True)

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? tz( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Tz`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Tz`
        """

        vis = shapes.Torus(float(self.c), float(self.b), float(self.a))
        vis = vis.translate(numpy.array((float(self.x), float(self.y), float(self.z))))

        return vis
