import re

from . import _field
from . import _surface
from .. import _show
from .. import types
from .. import errors


class Py(_surface.Surface):
    """
    Represents INP `py` surface cards.
    """

    _KEYWORD = 'py'

    d = _field.Field(types.Real, 'Normal-to-the-y-axis plane D coefficent', required=True, code=errors.InpCode.SEMANTICS_OPTION)

    _REGEX = re.compile(rf'\A(\+|\*)?(\S+)( \S+)? py( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Py`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Py`
        """

        vis = shapes.Plane(0, 1, 0, float(self.d))

        return vis
