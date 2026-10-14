import re

from . import _field
from . import _card
from .. import types


class Print(_field.Fields, _card.Card):
    """
    Represents INP `print` cards.
    """

    _KEYWORD = 'print'

    tables = _field.Field.tuple(types.Integer, 'Tables to print', numeric=int)

    _REGEX = re.compile(rf'\Aprint((?: {types.Integer._REGEX.pattern[2:-2]})+?)?\Z', re.IGNORECASE)
