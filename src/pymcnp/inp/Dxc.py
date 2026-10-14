import re

from . import _field
from . import _card
from .. import types


class Dxc(_field.Fields, _card.Card):
    """
    Represents INP `dxc` cards.
    """

    _KEYWORD = 'dxc'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not value <= 99999999)
    designator = _field.Field(types.Designator, 'Data card particle designator', required=True, numeric=())
    probabilities = _field.Field.tuple(types.Real, 'Probability of contribution to DXTRAN', required=True)

    _REGEX = re.compile(rf'\Adxc(\d+):(\S+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
