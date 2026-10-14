import re

from . import _field
from . import _surface
from .. import _show
from .. import types
from .. import errors


class So(_surface.Surface):
    """
    Represents INP `so` surface cards.
    """

    _KEYWORD = 'so'

    r = _field.Field(types.Real, 'Origin-centered sphere radius', required=True, code=errors.InpCode.SEMANTICS_OPTION)

    _REGEX = re.compile(rf'\A(\+|\*)?(\S+)( \S+)? so( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `So`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `So`
        """

        vis = shapes.Sphere(float(self.r))

        return vis
