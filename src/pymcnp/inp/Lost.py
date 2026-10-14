import re

from . import _field
from . import _card
from .. import types


class Lost(_field.Fields, _card.Card):
    """
    Represents INP `lost` cards.
    """

    _KEYWORD = 'lost'

    lost1 = _field.Field(types.Integer, 'Number of particles which can be lost before job termination', required=True, numeric=int, invalid=lambda self, value: not value >= 0)
    lost2 = _field.Field(types.Integer, 'Maximum number of debug prints for lost particles', required=True, numeric=int, invalid=lambda self, value: not value >= 0)

    _REGEX = re.compile(rf'\Alost( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
