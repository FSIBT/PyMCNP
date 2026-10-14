import re

from .. import _field
from . import _option
from ... import types


class Old(_field.Fields, _option.SsrOption):
    """
    Represents INP `old` elements.
    """

    _KEYWORD = 'old'

    numbers = _field.Field.tuple(types.Integer, 'Tuple of surface numbers from subset of surfaces on SSW card', required=True, numeric=int)

    _REGEX = re.compile(rf'\Aold((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
