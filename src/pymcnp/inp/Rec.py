import re

import numpy

from . import _field
from . import _surface
from .. import _show
from .. import types
from .. import errors


class Rec(_surface.Surface):
    """
    Represents INP `rec` surface cards.
    """

    _KEYWORD = 'rec'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    vx = _field.Field(types.Real, 'Elliptical cylinder position vector x component', required=True)
    vy = _field.Field(types.Real, 'Elliptical cylinder position vector y component', required=True)
    vz = _field.Field(types.Real, 'Elliptical cylinder position vector z component', required=True)
    hx = _field.Field(types.Real, 'Elliptical cylinder height vector x component', required=True)
    hy = _field.Field(types.Real, 'Elliptical cylinder height vector y component', required=True)
    hz = _field.Field(types.Real, 'Elliptical cylinder height vector z component', required=True)
    v1x = _field.Field(types.Real, 'Elliptical cylinder major axis vector x component', required=True)
    v1y = _field.Field(types.Real, 'Elliptical cylinder major axis vector y component', required=True)
    v1z = _field.Field(types.Real, 'Elliptical cylinder major axis vector z component', required=True)
    v2x = _field.Field(types.Real, 'Elliptical cylinder minor axis vector x component', required=True)
    v2y = _field.Field(types.Real, 'Elliptical cylinder minor axis vector y component')
    v2z = _field.Field(types.Real, 'Elliptical cylinder minor axis vector z component')

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? rec( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Rec`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Rec`
        """

        v = numpy.array((float(self.vx), float(self.vy), float(self.vz)))
        h = numpy.array((float(self.hx), float(self.hy), float(self.hz)))
        v1 = numpy.array((float(self.v1x), float(self.v1y), float(self.v1z)))
        v2 = numpy.array((float(self.v2x), float(self.v2y), float(self.v2z)))

        cross = numpy.cross(v, numpy.array((0, 0, 1)))
        angle = numpy.degrees(numpy.arccos(v[2] / numpy.linalg.norm(v)))

        vis = shapes.CylinderElliptical(numpy.linalg.norm(h), numpy.linalg.norm(v1), numpy.linalg.norm(v2))
        vis = vis.rotate(cross, angle, (0, 0, 0))
        vis = vis.translate(v)

        return vis
