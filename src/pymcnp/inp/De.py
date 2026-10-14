import re

from . import _field
from . import _card
from .. import types


class De(_field.Fields, _card.Card):
    """
    Represents INP de cards.
    """

    _KEYWORD = 'de'

    _ORDER = ('suffix', 'values', 'method')

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not value <= 99999999)
    method = _field.Field(types.String, 'Interpolation method for energy table', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'log', 'lin'})
    values = _field.Field.tuple(types.Real, 'Energy values', required=True)

    _REGEX = re.compile(rf'\Ade(\d+)( (?:log|lin))?((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
