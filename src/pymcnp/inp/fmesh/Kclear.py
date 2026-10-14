import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Kclear(_field.Fields, _option.FmeshOption):
    """
    Represents INP `kclear` elements.
    """

    _KEYWORD = 'kclear'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    count = _field.Field(types.Integer, 'KCODE cycles between zeros', required=True, numeric=int)

    _REGEX = re.compile(rf'\Akclear( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
