import re

from ... import _field
from . import _option
from .... import types


class Ith(_field.Fields, _option.BlockOption):
    """
    Represents INP `ith` elements.
    """

    _KEYWORD = 'ith'

    setting = _field.Field(types.Integer, 'Direction/adjoint calculation control', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1})

    _REGEX = re.compile(rf'\Aith( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
