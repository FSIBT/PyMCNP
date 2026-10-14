import re
import math

import numpy

from . import _field
from . import _surface
from .. import _show
from .. import types
from .. import errors


class Rhp(_surface.Surface):
    """
    Represents INP `rhp` surface cards.
    """

    _KEYWORD = 'rhp'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    vx = _field.Field(types.Real, 'Hexagonal prism position vector x component', required=True)
    vy = _field.Field(types.Real, 'Hexagonal prism position vector y component', required=True)
    vz = _field.Field(types.Real, 'Hexagonal prism position vector z component', required=True)
    hx = _field.Field(types.Real, 'Hexagonal prism height vector x component', required=True)
    hy = _field.Field(types.Real, 'Hexagonal prism height vector y component', required=True)
    hz = _field.Field(types.Real, 'Hexagonal prism height vector z component', required=True)
    r1 = _field.Field(types.Real, 'Hexagonal prism facet #1 vector x component', required=True)
    r2 = _field.Field(types.Real, 'Hexagonal prism facet #1 vector y component', required=True)
    r3 = _field.Field(types.Real, 'Hexagonal prism facet #1 vector z component', required=True)
    s1 = _field.Field(types.Real, 'Hexagonal prism facet #2 vector x component')
    s2 = _field.Field(types.Real, 'Hexagonal prism facet #2 vector y component')
    s3 = _field.Field(types.Real, 'Hexagonal prism facet #2 vector z component')
    t1 = _field.Field(types.Real, 'Hexagonal prism facet #3 vector x component')
    t2 = _field.Field(types.Real, 'Hexagonal prism facet #3 vector y component')
    t3 = _field.Field(types.Real, 'Hexagonal prism facet #3 vector z component')

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? rhp( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Rhp`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Rhp`
        """

        v = numpy.array((float(self.vx), float(self.vy), float(self.vz)))
        h = numpy.array((float(self.hx), float(self.hy), float(self.hz)))
        r = numpy.array((float(self.r1), float(self.r2), float(self.r3)))
        s = numpy.array((float(self.s1), float(self.s2), float(self.s3)))
        t = numpy.array((float(self.t1), float(self.t2), float(self.t3)))

        cross = numpy.cross(v, numpy.array((0, 0, 1)))
        angle = numpy.degrees(numpy.arccos(v[2] / numpy.linalg.norm(v)))
        apothem_r = numpy.linalg.norm(r) * 2 / math.sqrt(3)
        apothem_s = numpy.linalg.norm(s) * 2 / math.sqrt(3)
        apothem_t = numpy.linalg.norm(t) * 2 / math.sqrt(3)

        vis = shapes.CylinderHexagonal(numpy.linalg.norm(h), apothem_r, apothem_s, apothem_t)
        vis = vis.rotate(cross, angle, (0, 0, 0))
        vis = vis.translate(v)

        return vis
