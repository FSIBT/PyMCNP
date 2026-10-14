import re

from . import _field
from . import _card
from .. import types


class Mx(_field.Fields, _card.Card):
    """
    Represents INP `mx` cards.
    """

    _KEYWORD = 'mx'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int)
    designator = _field.Field(types.Designator, 'Data card particle designator', required=True, numeric=())
    zaids = _field.Field.tuple(types.String, 'Zaid substitutions for particles', required=True, numeric=())

    _REGEX = re.compile(rf'\Amx(\d+):(\S+)((?: (?:{types.Zaid._REGEX.pattern[2:-2]}|j|model|0))+?)\Z', re.IGNORECASE)
