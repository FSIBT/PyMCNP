import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Alib(_field.Fields, _option.MOption_0):
    """
    Represents INP `alib` elements.
    """

    _KEYWORD = 'alib'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    abx = _field.Field(types.String, 'Default alpha table identifier', required=True, numeric=())

    _REGEX = re.compile(rf'\Aalib( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
