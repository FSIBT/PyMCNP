import re

import numpy

from . import _field
from . import _surface
from .. import _show
from .. import types
from .. import errors


class Ell(_surface.Surface):
    """
    Represents INP `ell` surface cards.
    """

    _KEYWORD = 'ell'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    v1x = _field.Field(types.Real, 'Ellipsoid focus #1 or center x component', required=True)
    v1y = _field.Field(types.Real, 'Ellipsoid focus #1 or center y component', required=True)
    v1z = _field.Field(types.Real, 'Ellipsoid focus #1 or center z component', required=True)
    v2x = _field.Field(types.Real, 'Ellipsoid focus #2 or major axis x component', required=True)
    v2y = _field.Field(types.Real, 'Ellipsoid focus #2 or major axis y component', required=True)
    v2z = _field.Field(types.Real, 'Ellipsoid focus #2 or major axis z component', required=True)
    rm = _field.Field(types.Real, 'Ellipsoid major/minor axis radius length', required=True)

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? ell( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Ell`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Ell`.
        """

        v1 = numpy.array((float(self.v1x), float(self.v1y), float(self.v1z)))
        v2 = numpy.array((float(self.v2x), float(self.v2y), float(self.v2z)))

        if self.rm > 0:
            center = numpy.array(((v2 - v1)[0] / 2 + v1[0], (v2 - v1)[1] / 2 + v1[1], (v2 - v1)[2] / 2 + v1[2]))
            major_length = float(self.rm)
            minor_length = 2 * (((major_length / 2) ** 2 - (numpy.linalg.norm(v2 - v1) / 2) ** 2) ** 0.5)

            if numpy.linalg.norm(v2 - v1):
                cross = numpy.cross(v2 - v1, numpy.array((1, 0, 0)))
                angle = numpy.degrees(numpy.arccos((v2 - v1)[0] / numpy.linalg.norm(v2 - v1)))
            else:
                cross = None
                angle = 0
        if self.rm < 0:
            center = v1
            major_length = numpy.linalg.norm(v2)
            minor_length = -float(self.rm)
            cross = numpy.cross(v2, numpy.array((1, 0, 0)))
            angle = numpy.degrees(numpy.arccos(v2[0] / numpy.linalg.norm(v2)))

        vis = shapes.Ellipsoid(major_length, minor_length)
        if cross is not None:
            vis = vis.rotate(cross, angle, (0, 0, 0))
        vis = vis.translate(center)

        return vis
