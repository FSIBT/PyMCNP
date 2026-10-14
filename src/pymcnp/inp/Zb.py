import re

from . import _field
from . import _card
from .. import types


class Zb(_field.Fields, _card.Card):
    """
    Represents INP `zb` cards.
    """

    _KEYWORD = 'zb'

    anything = _field.Field(types.String, 'Any parameters', numeric=())

    _REGEX = re.compile(rf'\Azb( {types.String._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)
