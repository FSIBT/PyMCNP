import re

from ... import _field
from . import _option
from .... import types


class Tsaits(_field.Fields, _option.BlockOption):
    """
    Represents INP `tsaits` elements.
    """

    _KEYWORD = 'tsaits'

    setting = _field.Field(types.Integer, 'Maximum TSA iteration count', required=True, numeric=int)

    _REGEX = re.compile(rf'\Atsaits( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
