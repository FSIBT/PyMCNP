import re

from . import _field
from . import _card
from .. import types


class Mt(_field.Fields, _card.Card):
    """
    Represents INP `mt` cards.
    """

    _KEYWORD = 'mt'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int)
    identifiers = _field.Field.tuple(types.String, 'Corresponding S(α,β) identifier', required=True, numeric=())

    _REGEX = re.compile(rf'\Amt(\d+)((?: {types.String._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
