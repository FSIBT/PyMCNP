import re

from . import _field
from . import _card
from .. import types


class C(_field.Fields, _card.Card):
    """
    Represents INP c cards.
    """

    _KEYWORD = 'c'

    _ORDER = ('suffix', 'bounds', 'prefix', 't', 'c')

    prefix = _field.Field(types.String, 'Star prefix', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'*', '+'})
    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int)
    bounds = _field.Field.tuple(types.Real, 'Upper cosine bounds for bin', required=True)
    t = _field.Field(types.String, 'Notation to provide totals', numeric=())
    c = _field.Field(types.String, 'Notation to make bin values cumulative', numeric=())

    _REGEX = re.compile(rf'\A([*]?)c(\d+)((?: {types.Real._REGEX.pattern[2:-2]})+?)( {types.String._REGEX.pattern[2:-2]})?( {types.String._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)
