import re

from .. import _field
from . import _option
from ... import types


class New(_field.Fields, _option.SsrOption):
    """
    Represents INP `new` elements.
    """

    _KEYWORD = 'new'

    numbers = _field.Field.tuple(types.Integer, 'Tuple of surface numbers to start run', required=True, numeric=int)

    _REGEX = re.compile(rf'\Anew((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
