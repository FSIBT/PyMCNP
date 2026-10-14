import re

from . import _field
from . import _surface
from .. import _show
from .. import types
from .. import errors


class Px(_surface.Surface):
    """
    Represents INP `px` surface cards.
    """

    _KEYWORD = 'px'

    d = _field.Field(types.Real, 'Normal-to-the-x-axis plane D coefficent', required=True, code=errors.InpCode.SEMANTICS_OPTION)

    _REGEX = re.compile(rf'\A(\+|\*)?(\S+)( \S+)? px( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Px`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Px`
        """

        vis = shapes.Plane(1, 0, 0, float(self.d))

        return vis
