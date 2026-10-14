import re

from .. import _field
from . import _option
from ... import types


class F(_field.Fields, _option.StopOption):
    """
    Represents INP `f` elements.
    """

    _KEYWORD = 'f'

    suffix = _field.Field(types.Integer, 'Data card option option suffix', required=True, numeric=int, invalid=lambda self, value: not value <= 99999999)
    e = _field.Field(types.Integer, 'Tally fluctuation relative error before stop', required=True, numeric=int)

    _REGEX = re.compile(rf'\Af(\d+)( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
