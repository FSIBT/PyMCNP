import re

from .. import _field
from . import _option
from ... import types


class Nonu(_field.Fields, _option.CellOption):
    """
    Represents INP `nonu` elements.
    """

    _KEYWORD = 'nonu'

    setting = _field.Field(types.Integer, 'Cell fission setting', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1, 2})

    _REGEX = re.compile(rf'\Anonu( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
