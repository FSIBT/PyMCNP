import re

from . import _field
from . import _card
from .. import types


class Unc(_field.Fields, _card.Card):
    """
    Represents INP `unc` cards.
    """

    _KEYWORD = 'unc'

    designator = _field.Field(types.Designator, 'Data option particle designator', required=True, numeric=())
    settings = _field.Field.tuple(types.Integer, 'Tuple of uncollided secondary settings', required=True, numeric=int)

    _REGEX = re.compile(rf'\Aunc:(\S+)((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
