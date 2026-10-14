import re

from . import _field
from . import _card
from .. import types


class Awtab(_field.Fields, _card.Card):
    """
    Represents INP awtab cards.
    """

    _KEYWORD = 'awtab'

    weight_ratios = _field.Field.tuple(types.Substance, 'Tuple of atomic weight ratios', required=True, numeric=())

    _REGEX = re.compile(rf'\Aawtab((?: {types.Substance._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
