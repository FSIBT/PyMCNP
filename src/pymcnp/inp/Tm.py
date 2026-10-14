import re

from . import _field
from . import _card
from .. import types


class Tm(_field.Fields, _card.Card):
    """
    Represents INP `tm` cards.
    """

    _KEYWORD = 'tm'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not value <= 99999999)
    multipliers = _field.Field.tuple(types.Real, 'Time bin multiplier to apply', required=True)

    _REGEX = re.compile(rf'\Atm(\d+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
