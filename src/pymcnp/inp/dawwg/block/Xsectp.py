import re

from ... import _field
from . import _option
from .... import types
from .... import errors


class Xsectp(_field.Fields, _option.BlockOption):
    """
    Represents INP `xsectp` elements.
    """

    _KEYWORD = 'xsectp'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.Integer, 'Cross-section print flag', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1, 2})

    _REGEX = re.compile(rf'\Axsectp( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
