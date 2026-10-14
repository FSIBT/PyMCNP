import re

from . import _field
from . import _card
from .. import types


class Bflcl(_field.Fields, _card.Card):
    """
    Represents INP bflcl cards.
    """

    _KEYWORD = 'bflcl'

    numbers = _field.Field.tuple(types.Integer, 'Tuple of BFLD map numbers', required=True, numeric=int)

    _REGEX = re.compile(rf'\Abflcl((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
