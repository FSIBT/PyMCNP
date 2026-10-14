import re

import numpy

from . import _field
from . import _surface
from .. import _show
from .. import types
from .. import errors


class K_z(_surface.Surface):
    """
    Represents INP `k/z` surface cards.
    """

    _KEYWORD = 'k/z'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    x = _field.Field(types.Real, 'Parallel-to-z-axis cone center x component', required=True)
    y = _field.Field(types.Real, 'Parallel-to-z-axis cone center y component', required=True)
    z = _field.Field(types.Real, 'Parallel-to-z-axis cone center z component', required=True)
    t_squared = _field.Field(types.Real, 'Parallel-to-z-axis cone t^2 coefficent', required=True)
    plusminus_1 = _field.Field(types.Real, 'Parallel-to-z-axis cone sheet selector', required=True)

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? k/z( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `K_z`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `K_z`.
        """

        vis = shapes.ConeUnbounded(float(self.t_squared) ** (1 / 2), float(self.plusminus_1))
        vis = vis.translate(numpy.array((float(self.x), float(self.y), float(self.z))))

        return vis
