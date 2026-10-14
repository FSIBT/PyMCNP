import re

import numpy

from . import _field
from . import _surface
from .. import _show
from .. import types
from .. import errors


class Trc(_surface.Surface):
    """
    Represents INP `trc` surface cards.
    """

    _KEYWORD = 'trc'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    vx = _field.Field(types.Real, 'Truncated cone position vector x component', required=True)
    vy = _field.Field(types.Real, 'Truncated cone position vector y component', required=True)
    vz = _field.Field(types.Real, 'Truncated cone position vector z component', required=True)
    hx = _field.Field(types.Real, 'Truncated cone height vector x component', required=True)
    hy = _field.Field(types.Real, 'Truncated cone height vector y component', required=True)
    hz = _field.Field(types.Real, 'Truncated cone height vector z component', required=True)
    r1 = _field.Field(types.Real, 'Truncated cone lower cone radius', required=True)
    r2 = _field.Field(types.Real, 'Truncated cone upper cone radius', required=True)

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? trc( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Trc`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Trc`
        """

        h = numpy.array((float(self.hx), float(self.hy), float(self.hz)))

        cross = numpy.cross(h, numpy.array((0, 0, 1)))
        angle = numpy.degrees(numpy.arccos(h[2] / numpy.linalg.norm(h)))

        vis = shapes.ConeTruncated(numpy.linalg.norm(h), float(self.r1), float(self.r2))
        vis = vis.rotate(cross, angle, (0, 0, 0))
        vis = vis.translate(numpy.array((float(self.vx), float(self.vy), float(self.vz))))

        return vis
