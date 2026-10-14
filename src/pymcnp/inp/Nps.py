import re

from . import _field
from . import _card
from .. import types


class Nps(_field.Fields, _card.Card):
    """
    Represents INP `nps` cards.
    """

    _KEYWORD = 'nps'

    npp = _field.Field(types.Integer, 'Total number of histories to run', required=True, numeric=int, invalid=lambda self, value: not value > 0)
    npsmg = _field.Field(types.Integer, 'Number of history with direct source contributions', numeric=int, invalid=lambda self, value: value is not None and (not value > 0))

    _REGEX = re.compile(rf'\Anps( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)
