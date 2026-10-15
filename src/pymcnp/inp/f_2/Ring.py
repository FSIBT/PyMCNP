import re

from .. import _field
from . import _entry
from ... import types


class Ring(_field.Fields, _entry.FEntry_2):
    """
    Represents INP `ring` elements.
    """

    _KEYWORD = ''

    distance = _field.Field(types.Real, 'Ring position', required=True)
    radius = _field.Field(types.Real, 'Ring radius', required=True)
    ro = _field.Field(types.Real, 'Radius of sphere of exclusion', required=True)

    _REGEX = re.compile(rf'\A({types.Real._REGEX.pattern[2:-2]}) ({types.Real._REGEX.pattern[2:-2]}) ({types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
