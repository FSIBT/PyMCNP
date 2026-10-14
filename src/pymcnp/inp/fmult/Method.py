import re

from .. import _field
from . import _option
from ... import types


class Method(_field.Fields, _option.FmultOption):
    """
    Represents INP `method` elements.
    """

    _KEYWORD = 'method'

    setting = _field.Field(types.Integer, 'Gaussian sampling algorithm setting', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1, 3, 5, 6, 7})

    _REGEX = re.compile(rf'\Amethod( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
