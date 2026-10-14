import re

from . import _field
from . import _card
from .. import types


class Zc(_field.Fields, _card.Card):
    """
    Represents INP `zc` cards.
    """

    _KEYWORD = 'zc'

    anything = _field.Field(types.String, 'Any parameters', numeric=())

    _REGEX = re.compile(rf'\Azc( {types.String._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)
