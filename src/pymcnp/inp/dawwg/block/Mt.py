import re

from ... import _field
from . import _option
from .... import types


class Mt(_field.Fields, _option.BlockOption):
    """
    Represents INP `mt` elements.
    """

    _KEYWORD = 'mt'

    setting = _field.Field(types.Integer, 'Number of materials', required=True, numeric=int)

    _REGEX = re.compile(rf'\Amt( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
