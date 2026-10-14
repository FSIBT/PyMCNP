import re

import numpy

from . import _field
from . import _surface
from .. import _show
from .. import types
from .. import errors


class K_x(_surface.Surface):
    """
    Represents INP `k/x` surface cards.
    """

    _KEYWORD = 'k/x'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    x = _field.Field(types.Real, 'Parallel-to-x-axis cone center x component', required=True)
    y = _field.Field(types.Real, 'Parallel-to-x-axis cone center y component', required=True)
    z = _field.Field(types.Real, 'Parallel-to-x-axis cone center z component', required=True)
    t_squared = _field.Field(types.Real, 'Parallel-to-x-axis cone t^2 coefficent', required=True)
    plusminus_1 = _field.Field(types.Real, 'Parallel-to-x-axis cone sheet selector', required=True)

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? k/x( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `K_x`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `K_x`.
        """

        vis = shapes.ConeUnbounded(float(self.t_squared) ** (1 / 2), float(self.plusminus_1))
        vis = vis.rotate(numpy.array((0, 1, 0)), 90, (0, 0, 0))
        vis = vis.translate(numpy.array((float(self.x), float(self.y), float(self.z))))

        return vis
