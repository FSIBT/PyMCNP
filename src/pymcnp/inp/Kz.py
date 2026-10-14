import re

import numpy

from . import _field
from . import _surface
from .. import _show
from .. import types
from .. import errors


class Kz(_surface.Surface):
    """
    Represents INP `kz` surface cards.
    """

    _KEYWORD = 'kz'

    z = _field.Field(types.Real, 'On-z-axis cone center z component', required=True, code=errors.InpCode.SEMANTICS_OPTION)
    t_squared = _field.Field(types.Real, 'On-z-axis cone t^2 coefficent', required=True, code=errors.InpCode.SEMANTICS_OPTION)
    plusminus_1 = _field.Field(types.Real, 'On-z-axis cone sheet selector', required=True, code=errors.InpCode.SEMANTICS_OPTION)

    _REGEX = re.compile(rf'\A(\+|\*)?(\S+)( \S+)? kz( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Kz`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Kz`.
        """

        vis = shapes.ConeUnbounded(float(self.t_squared) ** (1 / 2), float(self.plusminus_1))
        vis = vis.translate(numpy.array((0, 0, float(self.z))))

        return vis
