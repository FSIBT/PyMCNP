import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Z_1(_field.Fields, _option.SdefOption):
    """
    Represents INP `z` elements variation #1.
    """

    _KEYWORD = 'z'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    position = _field.Field(types.Distribution, 'Position z-component', required=True, numeric=())

    _REGEX = re.compile(rf'\Az( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
