import re

from . import _field
from . import ssw
from . import _card
from .. import types


class Ssw(_field.Fields, _card.Card):
    """
    Represents INP `ssw` cards.
    """

    _KEYWORD = 'ssw'

    surfaces = _field.Field.tuple(types.Integer, 'Problem surfaces', required=True, numeric=int)
    cells = _field.Field.tuple(types.Integer, 'Problem cells', numeric=int)
    options = _field.Field.tuple(ssw.SswOption, 'Dictionary of options', numeric=())

    _REGEX = re.compile(rf'\Assw((?: {types.Integer._REGEX.pattern[2:-2]})+?)((?: {types.Integer._REGEX.pattern[2:-2]})+?)?((?: (?:{ssw.SswOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)
