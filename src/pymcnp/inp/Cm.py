import re

from . import _field
from . import _card
from .. import types


class Cm(_field.Fields, _card.Card):
    """
    Represents INP cm cards.
    """

    _KEYWORD = 'cm'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not value <= 99999999)
    multipliers = _field.Field.tuple(types.Real, 'Cosine bin multiplier to apply', required=True)

    _REGEX = re.compile(rf'\Acm(\d+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
