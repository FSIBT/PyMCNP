import re

from . import _field
from . import _surface
from .. import types
from .. import errors


class Sq(_surface.Surface):
    """
    Represents INP `sq` surface cards.
    """

    _KEYWORD = 'sq'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    a = _field.Field(types.Real, 'Oblique special quadratic A coefficent', required=True)
    b = _field.Field(types.Real, 'Oblique special quadratic B coefficent', required=True)
    c = _field.Field(types.Real, 'Oblique special quadratic C coefficent', required=True)
    d = _field.Field(types.Real, 'Oblique special quadratic D coefficent', required=True)
    e = _field.Field(types.Real, 'Oblique special quadratic E coefficent', required=True)
    f = _field.Field(types.Real, 'Oblique special quadratic F coefficent', required=True)
    g = _field.Field(types.Real, 'Oblique special quadratic G coefficent', required=True)
    x = _field.Field(types.Real, 'Oblique special quadratic center x component', required=True)
    y = _field.Field(types.Real, 'Oblique special quadratic center y component', required=True)
    z = _field.Field(types.Real, 'Oblique special quadratic center z component', required=True)

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? sq( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )
