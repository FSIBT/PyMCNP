import re

from .. import _field
from . import _option
from ... import types


class Kclear(_field.Fields, _option.FmeshOption):
    """
    Represents INP `kclear` elements.
    """

    _KEYWORD = 'kclear'

    count = _field.Field(types.Integer, 'KCODE cycles between zeros', required=True, numeric=int)

    _REGEX = re.compile(rf'\Akclear( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
