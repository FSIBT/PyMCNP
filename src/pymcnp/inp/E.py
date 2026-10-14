import re

from . import _field
from . import _card
from .. import types


class E(_field.Fields, _card.Card):
    """
    Represents INP `e` cards.
    """

    _KEYWORD = 'e'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int)
    bounds = _field.Field.tuple(types.Real, 'Upper energy bounds for bin', required=True)
    nt = _field.Field(types.String, 'Notation to inhibit automatic totaling', numeric=())
    c = _field.Field(types.String, 'Notation to make bin values cumulative', numeric=())

    _REGEX = re.compile(rf'\Ae(\d+)((?: {types.Real._REGEX.pattern[2:-2]})+?)( {types.String._REGEX.pattern[2:-2]})?( {types.String._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)
