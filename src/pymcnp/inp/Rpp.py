import re

from . import _field
from . import _surface
from .. import _show
from .. import types
from .. import errors


class Rpp(_surface.Surface):
    """
    Represents INP `rpp` surface cards.
    """

    _KEYWORD = 'rpp'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    xmin = _field.Field(types.Real, 'Parallelepiped x termini minimum', required=True)
    xmax = _field.Field(types.Real, 'Parallelepiped x termini maximum', required=True)
    ymin = _field.Field(types.Real, 'Parallelepiped y termini minimum', required=True)
    ymax = _field.Field(types.Real, 'Parallelepiped y termini maximum', required=True)
    zmin = _field.Field(types.Real, 'Parallelepiped z termini minimum')
    zmax = _field.Field(types.Real, 'Parallelepiped z termini maximum')

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? rpp( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Rpp`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Rpp`
        """

        vis = shapes.Parallelipiped(
            float(self.xmin),
            float(self.xmax),
            float(self.ymin),
            float(self.ymax),
            float(self.zmin),
            float(self.zmax),
        )

        return vis
