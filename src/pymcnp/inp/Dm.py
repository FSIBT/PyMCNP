import re

from . import _field
from . import _card
from .. import types


class Dm(_field.Fields, _card.Card):
    """
    Represents INP `dm` cards.
    """

    _KEYWORD = 'dm'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int)
    zaids = _field.Field.tuple(types.Zaid, 'Tuple of ZAID aliases', required=True, numeric=())

    _REGEX = re.compile(rf'\Adm(\d+)((?: {types.Zaid._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
