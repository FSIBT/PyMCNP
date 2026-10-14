import re

from . import _field
from . import ksrc
from . import _card


class Ksrc(_field.Fields, _card.Card):
    """
    Represents INP `ksrc` cards.
    """

    _KEYWORD = 'ksrc'

    locations = _field.Field.tuple(ksrc.Location, 'Tuple of inital source points', required=True, numeric=())

    _REGEX = re.compile(rf'\Aksrc((?: {ksrc.Location._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
