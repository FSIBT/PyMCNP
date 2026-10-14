import re

from . import _field
from . import _card
from .. import types


class Em(_field.Fields, _card.Card):
    """
    Represents INP `em` cards.
    """

    _KEYWORD = 'em'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not value <= 99999999)
    multipliers = _field.Field.tuple(types.Real, 'Energy bin multiplier to apply', required=True)

    _REGEX = re.compile(rf'\Aem(\d+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
