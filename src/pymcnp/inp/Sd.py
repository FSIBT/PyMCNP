import re

from . import _field
from . import _card
from .. import types


class Sd(_field.Fields, _card.Card):
    """
    Represents INP `sd` cards.
    """

    _KEYWORD = 'sd'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not value <= 99999999)
    information = _field.Field.tuple(types.Real, 'Area, volume, or mass by segmented, surface/cell', required=True)

    _REGEX = re.compile(rf'\Asd(\d+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
