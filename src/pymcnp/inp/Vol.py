import re

from . import _field
from . import _card
from .. import types


class Vol(_field.Fields, _card.Card):
    """
    Represents INP `vol` cards.
    """

    _KEYWORD = 'vol'

    _ORDER = ('volumes', 'no')

    no = _field.Field(types.String, 'Volume calculation on/off', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'no'})
    volumes = _field.Field.tuple(types.Real, 'Tuple of cell volumes', required=True)

    _REGEX = re.compile(rf'\Avol(?: (no))?((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
