import re

from . import _field
from . import _card
from .. import types


class Otfdb(_field.Fields, _card.Card):
    """
    Represents INP `otfdb` cards.
    """

    _KEYWORD = 'otfdb'

    zaids = _field.Field.tuple(types.Zaid, 'Identifiers for the broadening tables', required=True, numeric=())

    _REGEX = re.compile(rf'\Aotfdb((?: {types.Zaid._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
