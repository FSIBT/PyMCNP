import re

from . import _field
from . import _card
from .. import types


class Sf(_field.Fields, _card.Card):
    """
    Represents INP `sf` cards.
    """

    _KEYWORD = 'sf'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not value <= 99999999)
    numbers = _field.Field.tuple(types.Integer, 'Tallies for problem surface numbers to flag', required=True, numeric=int)

    _REGEX = re.compile(rf'\Asf(\d+)((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
