import re

import numpy

from . import _field
from . import _surface
from .. import _show
from .. import types
from .. import errors


class Rcc(_surface.Surface):
    """
    Represents INP `rcc` surface cards.
    """

    _KEYWORD = 'rcc'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    vx = _field.Field(types.Real, 'Circular cylinder macrobody position vector x component', required=True)
    vy = _field.Field(types.Real, 'Circular cylinder macrobody position vector y component', required=True)
    vz = _field.Field(types.Real, 'Circular cylinder macrobody position vector z component', required=True)
    hx = _field.Field(types.Real, 'Circular cylinder macrobody height vector x component', required=True)
    hy = _field.Field(types.Real, 'Circular cylinder macrobody height vector y component', required=True)
    hz = _field.Field(types.Real, 'Circular cylinder macrobody height vector z component', required=True)
    r = _field.Field(types.Real, 'Circular cylinder macrobody radius', required=True)

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? rcc( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Rcc`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Rcc`
        """

        v = numpy.array((float(self.vx), float(self.vy), float(self.vz)))
        h = numpy.array((float(self.hx), float(self.hy), float(self.hz)))

        height = numpy.linalg.norm(h)
        vis = shapes.CylinderCircular(height, float(self.r))

        if height > 0:
            h = h / height
            cross = numpy.cross(numpy.array((0, 0, 1)), h)
            angle = numpy.degrees(numpy.arccos(numpy.clip(h[2], -1, 1)))

            if numpy.linalg.norm(cross) > 1e-10:
                vis = vis.rotate(cross, angle, (0, 0, 0))

        vis = vis.translate(v)

        return vis
