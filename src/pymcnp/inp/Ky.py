import re

import numpy

from . import _field
from . import _surface
from .. import _show
from .. import types
from .. import errors


class Ky(_surface.Surface):
    """
    Represents INP `ky` surface cards.
    """

    _KEYWORD = 'ky'

    y = _field.Field(types.Real, 'On-y-axis cone center y component', required=True, code=errors.InpCode.SEMANTICS_OPTION)
    t_squared = _field.Field(types.Real, 'On-y-axis cone t^2 coefficent', required=True, code=errors.InpCode.SEMANTICS_OPTION)
    plusminus_1 = _field.Field(types.Real, 'On-y-axis cone sheet selector', required=True, code=errors.InpCode.SEMANTICS_OPTION)

    _REGEX = re.compile(rf'\A(\+|\*)?(\S+)( \S+)? ky( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Ky`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Ky`.
        """

        vis = shapes.ConeUnbounded(float(self.t_squared) ** (1 / 2), float(self.plusminus_1))
        vis = vis.rotate(numpy.array((1, 0, 0)), 90, (0, 0, 0))
        vis = vis.translate(numpy.array((0, float(self.y), 0)))

        return vis
