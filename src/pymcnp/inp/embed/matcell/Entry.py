import re

from ... import _field
from . import _entry
from .... import types


class Entry(_field.Fields, _entry.MatcellEntry):
    """
    Represents INP `entry` elements.
    """

    _KEYWORD = ''

    material = _field.Field(types.Integer, 'Material number', required=True, numeric=int, invalid=lambda self, value: not 0 <= value.value <= 99999999)
    cell = _field.Field(types.Integer, 'Geometry number', required=True, numeric=int, invalid=lambda self, value: not 0 <= value.value <= 99999999)

    _REGEX = re.compile(rf'\A({types.Integer._REGEX.pattern[2:-2]}) ({types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
