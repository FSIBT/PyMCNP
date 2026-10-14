import re

from . import _field
from . import _card
from .. import types


class Sb_0(_field.Fields, _card.Card):
    """
    Represents INP `sb` elements variation #0.
    """

    _KEYWORD = 'sb'

    _ORDER = ('suffix', 'biases', 'option')

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not (value >= 1 and value <= 999))
    option = _field.Field(types.String, 'Bias kind setting', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'d', 'c', 'v', 'w'})
    biases = _field.Field.tuple(types.Real, 'Particle source biases', required=True)

    _REGEX = re.compile(rf'\Asb(\d+)( [dcvw])?((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
