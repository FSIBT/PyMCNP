import re

from . import _field
from . import _card
from .. import types


class Embtb(_field.Fields, _card.Card):
    """
    Represents INP `embtb` cards.
    """

    _KEYWORD = 'embtb'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int)
    bounds = _field.Field.tuple(types.Real, 'Tuple of upper time bounds', required=True)

    _REGEX = re.compile(rf'\Aembtb(\d+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
