import re

from . import _field
from . import _card
from .. import types


class Embem(_field.Fields, _card.Card):
    """
    Represents INP `embem` cards.
    """

    _KEYWORD = 'embem'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int)
    multipliers = _field.Field.tuple(types.Real, 'Tuple of energy multipliers', required=True)

    _REGEX = re.compile(rf'\Aembem(\d+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
