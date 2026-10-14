import re

from ... import _field
from . import _option
from .... import types
from .... import errors


class Fmmix(_field.Fields, _option.BlockOption):
    """
    Represents INP `fmmix` elements.
    """

    _KEYWORD = 'fmmix'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.Integer, 'Read composition from LNK3DNT on/off', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1})

    _REGEX = re.compile(rf'\Afmmix( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
