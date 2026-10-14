import re

from . import _field
from . import _card
from .. import types


class U(_field.Fields, _card.Card):
    """
    Represents INP `u` cards.
    """

    _KEYWORD = 'u'

    numbers = _field.Field.tuple(types.Integer, 'Tuple of cell numbers', required=True, numeric=int)

    _REGEX = re.compile(rf'\Au((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
