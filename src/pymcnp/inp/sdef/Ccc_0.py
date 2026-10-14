import re

from .. import _field
from . import _option
from ... import types


class Ccc_0(_field.Fields, _option.SdefOption):
    """
    Represents INP `ccc` elements variation #0.
    """

    _KEYWORD = 'ccc'

    number = _field.Field(types.Integer, 'Cookie-cutter cell number', required=True, numeric=int, invalid=lambda self, value: not (value >= 0 and value <= 99999999))

    _REGEX = re.compile(rf'\Accc( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
