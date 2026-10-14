import re

from . import _field
from . import _card
from .. import types


class Mode(_field.Fields, _card.Card):
    """
    Represents INP `mode` cards.
    """

    _KEYWORD = 'mode'

    particles = _field.Field.tuple(types.Designator, 'Tuple of particle designators', required=True, numeric=())

    _REGEX = re.compile(rf'\Amode((?: {types.Designator._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
