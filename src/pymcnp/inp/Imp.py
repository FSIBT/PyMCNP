import re

from . import _field
from . import _card
from .. import types


class Imp(_field.Fields, _card.Card):
    """
    Represents INP `imp` cards.
    """

    _KEYWORD = 'imp'

    designator = _field.Field(types.Designator, 'Data card particle designator', required=True, numeric=())
    importances = _field.Field.tuple(types.Real, 'Cell importance', required=True)

    _REGEX = re.compile(rf'\Aimp:(\S+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
