import re

from . import _field
from . import _card
from .. import types


class Area(_field.Fields, _card.Card):
    """
    Represents INP area cards.
    """

    _KEYWORD = 'area'

    areas = _field.Field.tuple(types.Real, 'Tuple of surface areas', required=True)

    _REGEX = re.compile(rf'\Aarea((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
