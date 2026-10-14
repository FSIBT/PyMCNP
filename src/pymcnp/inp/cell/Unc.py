import re

from .. import _field
from . import _option
from ... import types


class Unc(_field.Fields, _option.CellOption):
    """
    Represents INP `unc` elements.
    """

    _KEYWORD = 'unc'

    designator = _field.Field(types.Designator, 'Cell particle designator', required=True, numeric=())
    setting = _field.Field(types.Integer, 'Cell uncollided secondaries setting', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1})

    _REGEX = re.compile(rf'\Aunc:(\S+)( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
