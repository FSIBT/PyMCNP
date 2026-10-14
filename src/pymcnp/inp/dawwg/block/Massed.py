import re

from ... import _field
from . import _option
from .... import types
from .... import errors


class Massed(_field.Fields, _option.BlockOption):
    """
    Represents INP `massed` elements.
    """

    _KEYWORD = 'massed'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.Integer, 'Mass edits on/off', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1})

    _REGEX = re.compile(rf'\Amassed( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
