import re

from . import _field
from . import _card
from .. import types


class Ext(_field.Fields, _card.Card):
    """
    Represents INP `ext` cards.
    """

    _KEYWORD = 'ext'

    designator = _field.Field(types.Designator, 'Data card particle designator', required=True, numeric=())
    stretching = _field.Field.tuple(types.String, 'Stretching direction for the cell', required=True, numeric=())

    _REGEX = re.compile(rf'\Aext:(\S+)((?: {types.String._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
