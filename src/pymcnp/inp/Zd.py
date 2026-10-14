import re

from . import _field
from . import _card
from .. import types


class Zd(_field.Fields, _card.Card):
    """
    Represents INP `zd` cards.
    """

    _KEYWORD = 'zd'

    anything = _field.Field(types.String, 'Any parameters', numeric=())

    _REGEX = re.compile(rf'\Azd( {types.String._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)
