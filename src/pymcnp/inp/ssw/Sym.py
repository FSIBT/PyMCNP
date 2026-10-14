import re

from .. import _field
from . import _option
from ... import types


class Sym(_field.Fields, _option.SswOption):
    """
    Represents INP `sym` elements.
    """

    _KEYWORD = 'sym'

    setting = _field.Field(types.Integer, 'Symmetric option flag', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1, 2})

    _REGEX = re.compile(rf'\Asym( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
