import re

from . import _field
from . import _card
from .. import types


class Wwt(_field.Fields, _card.Card):
    """
    Represents INP `wwt` cards.
    """

    _KEYWORD = 'wwt'

    designator = _field.Field(types.Designator, 'Data card particle designator', required=True, numeric=())
    bounds = _field.Field.tuple(types.Real, 'Upper time bound', required=True)

    _REGEX = re.compile(rf'\Awwt:(\S+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
