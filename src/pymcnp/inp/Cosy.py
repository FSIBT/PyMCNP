import re

from . import _field
from . import _card
from .. import types


class Cosy(_field.Fields, _card.Card):
    """
    Represents INP cosy cards.
    """

    _KEYWORD = 'cosy'

    numbers = _field.Field.tuple(types.Integer, 'Tuple of COSY map numbers', required=True, numeric=int)

    _REGEX = re.compile(rf'\Acosy((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
