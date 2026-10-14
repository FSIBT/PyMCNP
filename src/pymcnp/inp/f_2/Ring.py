import re

from .. import _field
from . import _entry
from ... import types
from ... import errors


class Ring(_field.Fields, _entry.FEntry_2):
    """
    Represents INP `ring` elements.
    """

    _KEYWORD = ''

    _CODE = errors.InpCode.SEMANTICS_OPTION

    distance = _field.Field(types.Real, 'Ring position', required=True)
    radius = _field.Field(types.Real, 'Ring radius', required=True)
    ro = _field.Field(types.Integer, 'Ring radius', required=True, numeric=int)

    _REGEX = re.compile(rf'\A({types.Real._REGEX.pattern[2:-2]}) ({types.Real._REGEX.pattern[2:-2]}) ({types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
