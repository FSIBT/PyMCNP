import re

from . import _field
from . import _surface
from .. import types
from .. import errors


class X(_surface.Surface):
    """
    Represents INP `x` surface cards.
    """

    _KEYWORD = 'x'

    x1 = _field.Field(types.Real, 'X-axisymmetric point-defined surface point #1 x component', required=True, code=errors.InpCode.SEMANTICS_OPTION)
    r1 = _field.Field(types.Real, 'X-axisymmetric point-defined surface point #1 radius', required=True, code=errors.InpCode.SEMANTICS_OPTION)
    x2 = _field.Field(types.Real, 'X-axisymmetric point-defined surface point #2 x component')
    r2 = _field.Field(types.Real, 'X-axisymmetric point-defined surface point #2 radius')
    x3 = _field.Field(types.Real, 'X-axisymmetric point-defined surface point #3 x component')
    r3 = _field.Field(types.Real, 'X-axisymmetric point-defined surface point #3 radius')

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? x( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )
