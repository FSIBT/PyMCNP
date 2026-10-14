import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Cosy(_field.Fields, _option.LikeOption):
    """
    Represents INP `cosy` elements.
    """

    _KEYWORD = 'cosy'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    number = _field.Field(types.Integer, 'Gets `number`', required=True, numeric=int, invalid=lambda self, value: value not in {1, 2, 3, 4, 5, 6})

    _REGEX = re.compile(rf'\Acosy( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
