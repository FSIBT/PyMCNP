import re

from .. import _field
from . import _entry
from ... import types


class Diagnostic(_field.Fields, _entry.DdEntry):
    """
    Represents INP `diagnostic` elements.
    """

    _KEYWORD = ''

    playing_setting = _field.Field(types.Real, 'Criterion for playing Russian roulette for DXTRAN', required=True)
    printing_setting = _field.Field(types.Real, 'Criterion for printing diagnostics for large contributions for DXTRAN', required=True)

    _REGEX = re.compile(rf'\A({types.Real._REGEX.pattern[2:-2]}) ({types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
