import re

from . import _field
from . import _card
from .. import types


class Cf(_field.Fields, _card.Card):
    """
    Represents INP cf cards.
    """

    _KEYWORD = 'cf'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not (value <= 99_999_999))
    numbers = _field.Field.tuple(types.Integer, 'Tallies for problem cell numbers to flag', required=True, numeric=int)

    _REGEX = re.compile(rf'\Acf(\d+)((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
