import re

from . import _field
from . import _card
from .. import types


class Histp(_field.Fields, _card.Card):
    """
    Represents INP `histp` cards.
    """

    _KEYWORD = 'histp'

    lhist = _field.Field(types.Integer, 'Number of words written to a HISTP file', numeric=int)
    cells = _field.Field.tuple(types.Integer, 'Cell numbers', numeric=int)

    _REGEX = re.compile(rf'\Ahistp( {types.Integer._REGEX.pattern[2:-2]})?((?: {types.Integer._REGEX.pattern[2:-2]})+?)?\Z', re.IGNORECASE)
