import re

from . import _field
from . import _card
from .. import types


class Drxs(_field.Fields, _card.Card):
    """
    Represents INP `drxs` cards.
    """

    _KEYWORD = 'drxs'

    zaids = _field.Field.tuple(types.Zaid, 'Tuple of ZAID aliases', numeric=())

    _REGEX = re.compile(rf'\Adrxs((?: {types.Zaid._REGEX.pattern[2:-2]})+?)?\Z', re.IGNORECASE)
