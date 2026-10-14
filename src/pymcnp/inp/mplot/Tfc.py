import re

from .. import _field
from . import _option
from ... import types


class Tfc(_field.Fields, _option.MplotOption):
    """
    Represents INP `tfc` elements.
    """

    _KEYWORD = 'tfc'

    x = _field.Field(types.String, 'Independent variable selector', required=True, numeric=())

    _REGEX = re.compile(rf'\Atfc( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
