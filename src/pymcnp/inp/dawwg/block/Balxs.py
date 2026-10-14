import re

from ... import _field
from . import _option
from .... import types
from .... import errors


class Balxs(_field.Fields, _option.BlockOption):
    """
    Represents INP `balxs` elements.
    """

    _KEYWORD = 'balxs'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.Integer, 'Cross-section balance control', required=True, numeric=int, invalid=lambda self, value: value not in {-1, 0, 1})

    _REGEX = re.compile(rf'\Abalxs( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
