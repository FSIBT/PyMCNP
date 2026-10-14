import re

from . import _field
from . import _surface
from .. import types
from .. import errors


class Z(_surface.Surface):
    """
    Represents INP `z` surface cards.
    """

    _KEYWORD = 'z'

    z1 = _field.Field(types.Real, 'Z-axisymmetric point-defined surface point #1 z component', required=True, code=errors.InpCode.SEMANTICS_OPTION)
    r1 = _field.Field(types.Real, 'Z-axisymmetric point-defined surface point #1 radius', required=True, code=errors.InpCode.SEMANTICS_OPTION)
    z2 = _field.Field(types.Real, 'Z-axisymmetric point-defined surface point #2 z component')
    r2 = _field.Field(types.Real, 'Z-axisymmetric point-defined surface point #2 radius')
    z3 = _field.Field(types.Real, 'Z-axisymmetric point-defined surface point #3 z component')
    r3 = _field.Field(types.Real, 'Z-axisymmetric point-defined surface point #3 radius')

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? z( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )
