import re

from ... import _field
from . import _option
from .... import types
from .... import errors


class Libname(_field.Fields, _option.BlockOption):
    """
    Represents INP `libname` elements.
    """

    _KEYWORD = 'libname'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.String, 'Cross-section file name', required=True, numeric=())

    _REGEX = re.compile(rf'\Alibname( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
