import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Tlib(_field.Fields, _option.MOption_0):
    """
    Represents INP `tlib` elements.
    """

    _KEYWORD = 'tlib'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    abx = _field.Field(types.String, 'Default triton table identifier', required=True, numeric=())

    _REGEX = re.compile(rf'\Atlib( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
