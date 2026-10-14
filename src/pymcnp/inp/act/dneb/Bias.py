import re

from ... import _field
from . import _entry
from .... import types


class Bias(_field.Fields, _entry.DnebEntry):
    """
    Represents INP `bias` elements.
    """

    _KEYWORD = ''

    weight = _field.Field(types.Real, 'Weight for bias', required=True)
    energy = _field.Field(types.Real, 'Energy boundary for bias', required=True)

    _REGEX = re.compile(rf'\A({types.Real._REGEX.pattern[2:-2]}) ({types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
