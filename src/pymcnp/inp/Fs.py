import re

from . import _field
from . import _card
from .. import types


class Fs(_field.Fields, _card.Card):
    """
    Represents INP `fs` cards.
    """

    _KEYWORD = 'fs'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not value <= 99999999)
    numbers = _field.Field.tuple(types.Integer, 'Signed problem number of a segmenting surface', required=True, numeric=int)
    t = _field.Field(types.String, 'Notation to provide totals', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'t'})
    c = _field.Field(types.String, 'Notation to make bin values cumulative', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'c'})

    _REGEX = re.compile(rf'\Afs(\d+)((?: {types.Integer._REGEX.pattern[2:-2]})+?)( t)?( c)?\Z', re.IGNORECASE)
