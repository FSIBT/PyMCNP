import re

import numpy

from . import _field
from . import _surface
from .. import _show
from .. import types
from .. import errors


class Sph(_surface.Surface):
    """
    Represents INP `sph` surface cards.
    """

    _KEYWORD = 'sph'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    vx = _field.Field(types.Real, 'Sphere macrobody position vector x component', required=True)
    vy = _field.Field(types.Real, 'Sphere macrobody position vector y component', required=True)
    vz = _field.Field(types.Real, 'Sphere macrobody position vector z component', required=True)
    r = _field.Field(types.Real, 'Sphere macrobody radius', required=True)

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? sph( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE
    )

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Sph`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Sph`
        """

        vis = shapes.Sphere(float(self.r))
        vis = vis.translate(numpy.array((float(self.vx), float(self.vy), float(self.vz))))

        return vis
