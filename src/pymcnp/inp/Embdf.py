import re

from . import _field
from . import _card
from .. import types


class Embdf(_field.Fields, _card.Card):
    """
    Represents INP `embdf` cards.
    """

    _KEYWORD = 'embdf'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int)
    multipliers = _field.Field.tuple(types.Real, 'Tuple of dose energy multipliers', required=True)

    _REGEX = re.compile(rf'\Aembdf(\d+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
