import re

from . import _field
from . import _card
from .. import types


class Talnp(_field.Fields, _card.Card):
    """
    Represents INP `talnp` cards.
    """

    _KEYWORD = 'talnp'

    tallies = _field.Field.tuple(types.Integer, 'Tallies to exclude from output', numeric=int)

    _REGEX = re.compile(rf'\Atalnp((?: {types.Integer._REGEX.pattern[2:-2]})+?)?\Z', re.IGNORECASE)
