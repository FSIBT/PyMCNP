import re

from ... import _field
from . import _option
from .... import types
from .... import errors


class Oitm(_field.Fields, _option.BlockOption):
    """
    Represents INP `oitm` elements.
    """

    _KEYWORD = 'oitm'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.Integer, 'Maximum outer iteration count', required=True, numeric=int)

    _REGEX = re.compile(rf'\Aoitm( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
