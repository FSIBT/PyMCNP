import re

from . import _field
from . import _card
from .. import types


class Lat(_field.Fields, _card.Card):
    """
    Represents INP `lat` cards.
    """

    _KEYWORD = 'lat'

    type = _field.Field.tuple(types.Integer, 'Tuple of lattice types', required=True, numeric=int)

    _REGEX = re.compile(rf'\Alat((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
