import re

from . import _field
from . import _surface
from .. import types
from .. import errors


class Y(_surface.Surface):
    """
    Represents INP `y` surface cards.
    """

    _KEYWORD = 'y'

    y1 = _field.Field(types.Real, 'Y-axisymmetric point-defined surface point #1 y component', required=True, code=errors.InpCode.SEMANTICS_OPTION)
    r1 = _field.Field(types.Real, 'Y-axisymmetric point-defined surface point #1 radius', required=True, code=errors.InpCode.SEMANTICS_OPTION)
    y2 = _field.Field(types.Real, 'Y-axisymmetric point-defined surface point #2 y component')
    r2 = _field.Field(types.Real, 'Y-axisymmetric point-defined surface point #2 radius')
    y3 = _field.Field(types.Real, 'Y-axisymmetric point-defined surface point #3 y component')
    r3 = _field.Field(types.Real, 'Y-axisymmetric point-defined surface point #3 radius')

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? y( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )
