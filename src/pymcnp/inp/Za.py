import re

from . import _field
from . import _card
from .. import types


class Za(_field.Fields, _card.Card):
    """
    Represents INP `za` cards.
    """

    _KEYWORD = 'za'

    anything = _field.Field(types.String, 'Any parameters', numeric=())

    _REGEX = re.compile(rf'\Aza( {types.String._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)
