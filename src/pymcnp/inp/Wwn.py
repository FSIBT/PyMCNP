import re

from . import _field
from . import _card
from .. import types


class Wwn(_field.Fields, _card.Card):
    """
    Represents INP `wwn` cards.
    """

    _KEYWORD = 'wwn'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not value <= 99999999)
    designator = _field.Field(types.Designator, 'Data card particle designator', required=True, numeric=())
    bounds = _field.Field.tuple(types.Real, 'Lower weight bound', required=True)

    _REGEX = re.compile(rf'\Awwn(\d+):(\S+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
