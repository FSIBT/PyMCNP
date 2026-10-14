import re

from . import _field
from . import _card
from .. import types


class Fill(_field.Fields, _card.Card):
    """
    Represents INP `fill` cards.
    """

    _KEYWORD = 'fill'

    numbers = _field.Field.tuple(types.Integer, 'Tuple of universe numbers', required=True, numeric=int)

    _REGEX = re.compile(rf'\Afill((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
