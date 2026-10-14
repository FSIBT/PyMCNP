import re

from .. import _field
from . import _option
from ... import types


class Mt(_field.Fields, _option.MplotOption):
    """
    Represents INP `mt` elements.
    """

    _KEYWORD = 'mt'

    n = _field.Field(types.Integer, 'Reaction number to print', required=True, numeric=int)

    _REGEX = re.compile(rf'\Amt( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
