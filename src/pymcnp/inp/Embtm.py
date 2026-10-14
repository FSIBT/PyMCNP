import re

from . import _field
from . import _card
from .. import types


class Embtm(_field.Fields, _card.Card):
    """
    Represents INP `embtm` cards.
    """

    _KEYWORD = 'embtm'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int)
    multipliers = _field.Field.tuple(types.Real, 'Tuple of time multipliers', required=True)

    _REGEX = re.compile(rf'\Aembtm(\d+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
