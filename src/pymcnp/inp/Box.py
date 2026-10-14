import re

import numpy

from . import _field
from . import _surface
from .. import _show
from .. import types
from .. import errors


class Box(_surface.Surface):
    """
    Represents INP `box` surface cards.
    """

    _KEYWORD = 'box'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    vx = _field.Field(types.Real, 'Box macrobody position vector x component', required=True)
    vy = _field.Field(types.Real, 'Box macrobody position vector y component', required=True)
    vz = _field.Field(types.Real, 'Box macrobody position vector z component', required=True)
    a1x = _field.Field(types.Real, 'Box macrobody vector #1 x component', required=True)
    a1y = _field.Field(types.Real, 'Box macrobody vector #1 y component', required=True)
    a1z = _field.Field(types.Real, 'Box macrobody vector #1 z component', required=True)
    a2x = _field.Field(types.Real, 'Box macrobody vector #2 x component', required=True)
    a2y = _field.Field(types.Real, 'Box macrobody vector #2 y component', required=True)
    a2z = _field.Field(types.Real, 'Box macrobody vector #2 z component', required=True)
    a3x = _field.Field(types.Real, 'Box macrobody vector #3 x component', required=True)
    a3y = _field.Field(types.Real, 'Box macrobody vector #3 y component', required=True)
    a3z = _field.Field(types.Real, 'Box macrobody vector #3 z component', required=True)

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? box( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Box`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Box`.
        """

        v = numpy.array((float(self.vx), float(self.vy), float(self.vz)))
        a1 = numpy.array((float(self.a1x), float(self.a1y), float(self.a1z)))
        a2 = numpy.array((float(self.a2x), float(self.a2y), float(self.a2z)))
        a3 = numpy.array((float(self.a3x), float(self.a3y), float(self.a3z)))

        cross = numpy.cross(numpy.array((1, 0, 0)), a1)
        angle = numpy.degrees(numpy.arccos(a1[0] / numpy.linalg.norm(a1)))

        vis = shapes.Box(numpy.linalg.norm(a1), numpy.linalg.norm(a2), numpy.linalg.norm(a3))
        vis = vis.rotate(cross, angle, (0, 0, 0))
        vis = vis.translate(v + 0.5 * (a1 + a2 + a3))

        return vis
