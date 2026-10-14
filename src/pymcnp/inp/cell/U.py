import re

from .. import _field
from . import _option
from ... import types


class U(_field.Fields, _option.CellOption):
    """
    Represents INP `u` elements.
    """

    _KEYWORD = 'u'

    number = _field.Field(types.Integer, 'Cell universe number', required=True, numeric=int, invalid=lambda self, value: not (value == 10000000000 or (value >= -9 and value <= 99999999)))

    _REGEX = re.compile(rf'\Au( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
