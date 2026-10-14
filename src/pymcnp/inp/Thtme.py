import re

from . import _field
from . import _card
from .. import types


class Thtme(_field.Fields, _card.Card):
    """
    Represents INP `thtme` cards.
    """

    _KEYWORD = 'thtme'

    times = _field.Field.tuple(types.Real, 'Tuple of times when thermal temperatures are specified', required=True)

    _REGEX = re.compile(rf'\Athtme((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
