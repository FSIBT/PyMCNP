import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Xsec(_field.Fields, _option.DawwgOption):
    """
    Represents INP `xsec` elements.
    """

    _KEYWORD = 'xsec'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    name = _field.Field(types.String, 'Cross section library', required=True, numeric=())

    _REGEX = re.compile(rf'\Axsec( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
