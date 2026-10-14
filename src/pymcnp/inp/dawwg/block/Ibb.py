import re

from ... import _field
from . import _option
from .... import types
from .... import errors


class Ibb(_field.Fields, _option.BlockOption):
    """
    Represents INP `ibb` elements.
    """

    _KEYWORD = 'ibb'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.Integer, 'Bottom  boudary condition', required=True, numeric=int)

    _REGEX = re.compile(rf'\Aibb( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
