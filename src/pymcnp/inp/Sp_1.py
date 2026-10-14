import re

from . import _field
from . import _card
from .. import types


class Sp_1(_field.Fields, _card.Card):
    """
    Represents INP `sp` elements variation #1.
    """

    _KEYWORD = 'sp'

    function = _field.Field(types.Integer, 'Built-in function designator', required=True, numeric=int, invalid=lambda self, value: value not in {-2, -3, -4, -5, -6, -7, -21, -31, -41})
    a = _field.Field(types.Real, 'Built-in function parameter #1', required=True)
    b = _field.Field(types.Real, 'Built-in function parameter #2')

    _REGEX = re.compile(rf'\Asp( {types.Integer._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)
