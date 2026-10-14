import re

from . import _field
from . import _card
from .. import types


class Rdum(_field.Fields, _card.Card):
    """
    Represents INP `rdum` cards.
    """

    _KEYWORD = 'rdum'

    floats = _field.Field.tuple(types.Real, 'Floating point array', required=True)

    _REGEX = re.compile(rf'\Ardum((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
