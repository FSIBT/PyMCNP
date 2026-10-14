import re

import numpy

from . import _field
from . import _surface
from .. import _show
from .. import types
from .. import errors


class Ty(_surface.Surface):
    """
    Represents INP `ty` surface cards.
    """

    _KEYWORD = 'ty'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    x = _field.Field(types.Real, 'Parallel-to-y-axis tori center x component', required=True)
    y = _field.Field(types.Real, 'Parallel-to-y-axis tori center y component', required=True)
    z = _field.Field(types.Real, 'Parallel-to-y-axis tori center z component', required=True)
    a = _field.Field(types.Real, 'Parallel-to-y-axis tori A coefficent', required=True)
    b = _field.Field(types.Real, 'Parallel-to-y-axis tori B coefficent', required=True)
    c = _field.Field(types.Real, 'Parallel-to-y-axis tori C coefficent', required=True)

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? ty( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Ty`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Ty`
        """

        vis = shapes.Torus(float(self.b), float(self.c), float(self.a))
        vis = vis.rotate(numpy.array((1, 0, 0)), 90, (0, 0, 0))
        vis = vis.translate(numpy.array((float(self.x), float(self.y), float(self.z))))

        return vis
