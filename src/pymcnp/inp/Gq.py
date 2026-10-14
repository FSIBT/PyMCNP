import re

from . import _field
from . import _surface
from .. import types
from .. import errors


class Gq(_surface.Surface):
    """
    Represents INP `gq` surface cards.
    """

    _KEYWORD = 'gq'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    a = _field.Field(types.Real, 'Oblique special quadratic A coefficent', required=True)
    b = _field.Field(types.Real, 'Oblique special quadratic B coefficent', required=True)
    c = _field.Field(types.Real, 'Oblique special quadratic C coefficent', required=True)
    d = _field.Field(types.Real, 'Oblique special quadratic D coefficent', required=True)
    e = _field.Field(types.Real, 'Oblique special quadratic E coefficent', required=True)
    f = _field.Field(types.Real, 'Oblique special quadratic F coefficent', required=True)
    g = _field.Field(types.Real, 'Oblique special quadratic G coefficent', required=True)
    h = _field.Field(types.Real, 'Oblique special quadratic H coefficent', required=True)
    j = _field.Field(types.Real, 'Oblique special quadratic J coefficent', required=True)
    k = _field.Field(types.Real, 'Oblique special quadratic K coefficent', required=True)

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? gq( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )
