import re

from . import _field
from . import _card
from .. import types


class Mphys(_field.Fields, _card.Card):
    """
    Represents INP `mphys` cards.
    """

    _KEYWORD = 'mphys'

    setting = _field.Field(types.String, 'Physics models on/off', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'on', 'off'})

    _REGEX = re.compile(rf'\Amphys( {types.String._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)
