import re

from ... import _field
from . import _option
from .... import types
from .... import errors


class Asleft(_field.Fields, _option.BlockOption):
    """
    Represents INP `asleft` elements.
    """

    _KEYWORD = 'asleft'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.Integer, 'Right-going flux at plane i', required=True, numeric=int)

    _REGEX = re.compile(rf'\Aasleft( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
