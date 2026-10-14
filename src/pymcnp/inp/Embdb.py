import re

from . import _field
from . import _card
from .. import types


class Embdb(_field.Fields, _card.Card):
    """
    Represents INP `embdb` cards.
    """

    _KEYWORD = 'embdb'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int)
    bounds = _field.Field.tuple(types.Real, 'Tuple of upper dose energy bounds', required=True)

    _REGEX = re.compile(rf'\Aembdb(\d+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
