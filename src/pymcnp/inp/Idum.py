import re

from . import _field
from . import _card
from .. import types


class Idum(_field.Fields, _card.Card):
    """
    Represents INP `idum` cards.
    """

    _KEYWORD = 'idum'

    intergers = _field.Field.tuple(types.Integer, 'Integer array', required=True, numeric=int)

    _REGEX = re.compile(rf'\Aidum((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
