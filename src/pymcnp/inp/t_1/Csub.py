import re

from .. import _field
from . import _option
from ... import types


class Csub(_field.Fields, _option.TOption_1):
    """
    Represents INP `csub` elements.
    """

    _KEYWORD = 'csub'

    count = _field.Field(types.Integer, 'Number of subdivisions to use', required=True, numeric=int)

    _REGEX = re.compile(rf'\Acsub( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
