import re

from . import _field
from . import _card
from .. import types


class Wwge(_field.Fields, _card.Card):
    """
    Represents INP `wwge` cards.
    """

    _KEYWORD = 'wwge'

    designator = _field.Field(types.Designator, 'Data card particle designator', required=True, numeric=())
    bounds = _field.Field.tuple(types.Real, 'Upper energy bound for weight-window group to be generated', required=True)

    _REGEX = re.compile(rf'\Awwge:(\S+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
