import re

from . import _field
from . import _card


class Notrn(_field.Fields, _card.Card):
    """
    Represents INP `notrn` cards.
    """

    _KEYWORD = 'notrn'

    _REGEX = re.compile(r'\Anotrn\Z', re.IGNORECASE)
