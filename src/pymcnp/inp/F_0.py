import re

from . import _field
from . import _card
from .. import types


class F_0(_field.Fields, _card.Card):
    """
    Represents INP `f` elements variation #0.
    """

    _KEYWORD = 'f'

    _ORDER = ('suffix', 'problems', 'prefix', 'designator', 't')

    prefix = _field.Field(types.String, 'Star prefix', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'*', '+'})
    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not (value <= 99999999 and value % 10 in {1, 2, 4, 6, 7}))
    designator = _field.Field(types.Designator, 'Data card particle designator', numeric=())
    problems = _field.Field.tuple(types.Integer, 'Problem numbers of surface or cell', required=True, numeric=int)
    t = _field.Field(types.String, 'Notation to make bin values cumulative', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'t'})

    _REGEX = re.compile(rf'\A([*+])?f(\d*[123467])(?::(\S+))?((?: {types.Integer._REGEX.pattern[2:-2]})+?)( t)?\Z', re.IGNORECASE)
