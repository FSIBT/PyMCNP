import re

from .. import _field
from . import _option
from ... import types


class Maxdeflc(_field.Fields, _option.BfldOption):
    """
    Represents INP `maxdeflc` elements.
    """

    _KEYWORD = 'maxdeflc'

    angle = _field.Field(types.Real, 'Maximum deflection angles', required=True)

    _REGEX = re.compile(rf'\Amaxdeflc( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
