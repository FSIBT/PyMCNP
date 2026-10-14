import re

from . import _field
from . import _card
from .. import types


class Sp_0(_field.Fields, _card.Card):
    """
    Represents INP `sp` elements variation #0.
    """

    _KEYWORD = 'sp'

    _ORDER = ('suffix', 'probabilities', 'option')

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not (value >= 1 and value <= 999))
    option = _field.Field(types.String, 'Probability kind setting', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'d', 'c', 'v', 'w'})
    probabilities = _field.Field.tuple(types.Real, 'Particle source probabilities', required=True)

    _REGEX = re.compile(rf'\Asp(\d+)( [dcvw])?((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
