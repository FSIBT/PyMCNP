import re

from . import _field
from . import _surface
from .. import _show
from .. import types
from .. import errors


class Pz(_surface.Surface):
    """
    Represents INP `pz` surface cards.
    """

    _KEYWORD = 'pz'

    d = _field.Field(types.Real, 'Normal-to-the-z-axis plane D coefficent', required=True, code=errors.InpCode.SEMANTICS_OPTION)

    _REGEX = re.compile(rf'\A(\+|\*)?(\S+)( \S+)? pz( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Pz`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Pz`
        """

        vis = shapes.Plane(0, 0, 1, float(self.d))

        return vis
