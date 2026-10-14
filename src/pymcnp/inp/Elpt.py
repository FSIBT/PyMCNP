import re

from . import _field
from . import _card
from .. import types


class Elpt(_field.Fields, _card.Card):
    """
    Represents INP `elpt` cards.
    """

    _KEYWORD = 'elpt'

    cutoffs = _field.Field.tuple(types.Real, 'Tuple of cell lower energy cutoffs', required=True)

    _REGEX = re.compile(rf'\Aelpt((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
