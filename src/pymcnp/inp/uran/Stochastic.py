import re

from .. import _field
from . import _entry
from ... import types


class Stochastic(_field.Fields, _entry.UranEntry):
    """
    Represents INP `stochastic` elements.
    """

    _KEYWORD = ''

    universe = _field.Field(types.Integer, 'Universe number', required=True, numeric=int, invalid=lambda self, value: not 0 <= value.value <= 99999999)
    maximum_x = _field.Field(types.Real, 'Maximum x displacement', required=True)
    maximum_y = _field.Field(types.Real, 'Maximum y displacement', required=True)
    maximum_z = _field.Field(types.Real, 'Maximum z displacement', required=True)

    _REGEX = re.compile(rf'\A({types.Integer._REGEX.pattern[2:-2]}) ({types.Real._REGEX.pattern[2:-2]}) ({types.Real._REGEX.pattern[2:-2]}) ({types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
