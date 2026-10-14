import re

from .. import _field
from . import _option
from ... import types


class Kcode(_field.Fields, _option.MplotOption):
    """
    Represents INP `kcode` elements.
    """

    _KEYWORD = 'kcode'

    i = _field.Field(types.Integer, 'Lifetime to remove', required=True, numeric=int, invalid=lambda self, value: not (value >= 1 and value <= 6 or (value >= 1 and value <= 19)))

    _REGEX = re.compile(rf'\Akcode( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
