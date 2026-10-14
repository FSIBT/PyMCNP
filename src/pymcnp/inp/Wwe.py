import re

from . import _field
from . import _card
from .. import types


class Wwe(_field.Fields, _card.Card):
    """
    Represents INP `wwe` cards.
    """

    _KEYWORD = 'wwe'

    designator = _field.Field(types.Designator, 'Data card particle designator', required=True, numeric=())
    bounds = _field.Field.tuple(types.Real, 'Upper energy/time bound', required=True)

    _REGEX = re.compile(rf'\Awwe:(\S+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
