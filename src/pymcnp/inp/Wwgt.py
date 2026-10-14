import re

from . import _field
from . import _card
from .. import types


class Wwgt(_field.Fields, _card.Card):
    """
    Represents INP `wwgt` cards.
    """

    _KEYWORD = 'wwgt'

    designator = _field.Field(types.Designator, 'Data card particle designator', required=True, numeric=())
    bounds = _field.Field.tuple(types.Real, 'Upper time bound for weight-window group to be generated', required=True)

    _REGEX = re.compile(rf'\Awwgt:(\S+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
