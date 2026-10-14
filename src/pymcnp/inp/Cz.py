import re

from . import _field
from . import _surface
from .. import _show
from .. import types
from .. import errors


class Cz(_surface.Surface):
    """
    Represents INP `cz` surface cards.
    """

    _KEYWORD = 'cz'

    r = _field.Field(types.Real, 'On-z-axis cylinder radius', required=True, code=errors.InpCode.SEMANTICS_OPTION)

    _REGEX = re.compile(rf'\A(\+|\*)?(\S+)( \S+)? cz( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Cz`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Cz`.
        """

        vis = shapes.CylinderUnbounded(float(self.r))

        return vis
