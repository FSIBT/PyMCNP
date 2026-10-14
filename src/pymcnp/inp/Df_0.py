import re

from . import _field
from . import _card
from .. import types


class Df_0(_field.Fields, _card.Card):
    """
    Represents INP df cards variation #0.
    """

    _KEYWORD = 'df'

    _ORDER = ('suffix', 'values', 'method')

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not value <= 99999999)
    method = _field.Field(types.String, 'Interpolation method for dose function table', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'log', 'lin'})
    values = _field.Field.tuple(types.Real, 'Dose function values', required=True)

    _REGEX = re.compile(rf'\Adf(\d+)( (?:log|lin))?((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
