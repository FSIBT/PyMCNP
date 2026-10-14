import re

from . import _field
from . import _card
from .. import types


class Fu(_field.Fields, _card.Card):
    """
    Represents INP `fu` cards.
    """

    _KEYWORD = 'fu'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not value <= 99999999)
    bounds = _field.Field.tuple(types.Real, 'Input parameters for user bins', required=True)
    nt = _field.Field(types.String, 'Notation to inhibit automatic totaling', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'nt'})
    c = _field.Field(types.String, 'Notation to make bin values cumulative', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'c'})

    _REGEX = re.compile(rf'\Afu(\d+)((?: {types.Real._REGEX.pattern[2:-2]})+?)(?: (nt))?(?: (c))?\Z', re.IGNORECASE)
