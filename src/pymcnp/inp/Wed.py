import re

import numpy

from . import _field
from . import _surface
from .. import _show
from .. import types
from .. import errors


class Wed(_surface.Surface):
    """
    Represents INP `wed` surface cards.
    """

    _KEYWORD = 'wed'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    vx = _field.Field(types.Real, 'Wedge position vector x component', required=True)
    vy = _field.Field(types.Real, 'Wedge position vector y component', required=True)
    vz = _field.Field(types.Real, 'Wedge position vector z component', required=True)
    v1x = _field.Field(types.Real, 'Wedge side vector #1 x component', required=True)
    v1y = _field.Field(types.Real, 'Wedge side vector #1 y component', required=True)
    v1z = _field.Field(types.Real, 'Wedge side vector #1 z component', required=True)
    v2x = _field.Field(types.Real, 'Wedge side vector #2 x component', required=True)
    v2y = _field.Field(types.Real, 'Wedge side vector #2 y component', required=True)
    v2z = _field.Field(types.Real, 'Wedge side vector #2 z component', required=True)
    v3x = _field.Field(types.Real, 'Wedge height vector x component', required=True)
    v3y = _field.Field(types.Real, 'Wedge height vector y component', required=True)
    v3z = _field.Field(types.Real, 'Wedge height vector z component', required=True)

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? wed( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Wed`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Wed`
        """

        v = numpy.array((float(self.vx), float(self.vy), float(self.vz)))
        v1 = numpy.array((float(self.v1x), float(self.v1y), float(self.v1z)))
        v2 = numpy.array((float(self.v2x), float(self.v2y), float(self.v2z)))
        v3 = numpy.array((float(self.v3x), float(self.v3y), float(self.v3z)))

        cross = numpy.cross(numpy.array((1, 0, 0)), v1)
        angle = numpy.degrees(numpy.arccos(v1[0] / numpy.linalg.norm(v1)))

        vis = shapes.Wedge(numpy.linalg.norm(v1), numpy.linalg.norm(v2), numpy.linalg.norm(v3))
        vis = vis.rotate(cross, angle, (0, 0, 0))
        vis = vis.translate(v)

        return vis
