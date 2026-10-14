import re

import numpy

from . import _field
from . import _surface
from .. import _show
from .. import types
from .. import errors


class Kx(_surface.Surface):
    """
    Represents INP `kx` surface cards.
    """

    _KEYWORD = 'kx'

    x = _field.Field(types.Real, 'On-x-axis cone center x component', required=True, code=errors.InpCode.SEMANTICS_OPTION)
    t_squared = _field.Field(types.Real, 'On-x-axis cone t^2 coefficent', required=True, code=errors.InpCode.SEMANTICS_OPTION)
    plusminus_1 = _field.Field(types.Real, 'On-x-axis cone sheet selector', required=True, code=errors.InpCode.SEMANTICS_OPTION)

    _REGEX = re.compile(rf'\A(\+|\*)?(\S+)( \S+)? kx( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Kx`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Kx`.
        """

        vis = shapes.ConeUnbounded(float(self.t_squared) ** (1 / 2), float(self.plusminus_1))
        vis = vis.rotate(numpy.array((0, 1, 0)), 90, (0, 0, 0))
        vis = vis.translate(numpy.array((float(self.x), 0, 0)))

        return vis
