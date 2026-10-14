import re

from . import _field
from . import _card
from .. import types


class Embeb(_field.Fields, _card.Card):
    """
    Represents INP `embeb` cards.
    """

    _KEYWORD = 'embeb'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int)
    bounds = _field.Field.tuple(types.Real, 'Tuple of upper energy bounds', required=True)

    _REGEX = re.compile(rf'\Aembeb(\d+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
