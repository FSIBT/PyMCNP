import re

from .. import _field
from . import _option
from ... import types


class Col(_field.Fields, _option.SsrOption):
    """
    Represents INP `col` elements.
    """

    _KEYWORD = 'col'

    setting = _field.Field(types.Integer, 'Collision option setting', required=True, numeric=int, invalid=lambda self, value: value not in {-1, 0, 1})

    _REGEX = re.compile(rf'\Acol( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
