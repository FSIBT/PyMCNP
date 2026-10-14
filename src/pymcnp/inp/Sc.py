import re

from . import _field
from . import _card
from .. import types


class Sc(_field.Fields, _card.Card):
    """
    Represents INP `sc` cards.
    """

    _KEYWORD = 'sc'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not (value >= 1 and value <= 999))
    comment = _field.Field.tuple(types.String, 'Source comment', required=True, numeric=())

    _REGEX = re.compile(rf'\Asc(\d+)((?: {types.String._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
