import re

from .. import _field
from . import _option
from ... import types


class Nap(_field.Fields, _option.ActOption):
    """
    Represents INP `nap` elements.
    """

    _KEYWORD = 'nap'

    count = _field.Field(types.Integer, 'Number of activation products', required=True, numeric=int, invalid=lambda self, value: not value >= 0)

    _REGEX = re.compile(rf'\Anap( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
