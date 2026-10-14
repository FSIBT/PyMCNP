import re

from . import _field
from . import _card
from .. import types


class Nonu(_field.Fields, _card.Card):
    """
    Represents INP `nonu` cards.
    """

    _KEYWORD = 'nonu'

    settings = _field.Field.tuple(types.Integer, 'Tuple of fission settings', numeric=int)

    _REGEX = re.compile(rf'\Anonu((?: {types.Integer._REGEX.pattern[2:-2]})+?)?\Z', re.IGNORECASE)
