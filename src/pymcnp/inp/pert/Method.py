import re

from .. import _field
from . import _option
from ... import types


class Method(_field.Fields, _option.PertOption):
    """
    Represents INP `method` elements.
    """

    _KEYWORD = 'method'

    setting = _field.Field(types.Integer, 'Printing and specifies setting', required=True, numeric=int, invalid=lambda self, value: value not in {1, -1, 2, -2, 3, -3})

    _REGEX = re.compile(rf'\Amethod( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
