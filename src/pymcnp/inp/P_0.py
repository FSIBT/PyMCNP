import re

from . import _field
from . import _surface
from .. import _show
from .. import types
from .. import errors


class P_0(_surface.Surface):
    """
    Represents INP `p` surface cards variation #0.
    """

    _KEYWORD = 'p'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    a = _field.Field(types.Real, 'Equation-defined general plane A coefficent', required=True)
    b = _field.Field(types.Real, 'Equation-defined general plane B coefficent', required=True)
    c = _field.Field(types.Real, 'Equation-defined general plane C coefficent', required=True)
    d = _field.Field(types.Real, 'Equation-defined general plane D coefficent', required=True)

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? p( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE
    )

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Px`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Px`
        """

        vis = shapes.Plane(float(self.a), float(self.b), float(self.c), float(self.d))

        return vis
