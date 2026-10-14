import re

from . import _field
from . import _card
from .. import types


class Tmp(_field.Fields, _card.Card):
    """
    Represents INP `tmp` cards.
    """

    _KEYWORD = 'tmp'

    _ORDER = ('temperatures', 'suffix')

    suffix = _field.Field(types.Integer, 'Data card option suffix', numeric=int)
    temperatures = _field.Field.tuple(types.Real, 'Cell temperatrues', required=True)

    _REGEX = re.compile(rf'\Atmp(\d+)?((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
