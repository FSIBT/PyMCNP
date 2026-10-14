import re

from . import _field
from . import _card
from .. import types


class Void(_field.Fields, _card.Card):
    """
    Represents INP `void` cards.
    """

    _KEYWORD = 'void'

    numbers = _field.Field.tuple(types.Integer, 'Tuple of cell numbers', numeric=int)

    _REGEX = re.compile(rf'\Avoid((?: {types.Integer._REGEX.pattern[2:-2]})+?)?\Z', re.IGNORECASE)
