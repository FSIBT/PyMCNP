import re

from ... import _field
from . import _option
from .... import types
from .... import errors


class Pted(_field.Fields, _option.BlockOption):
    """
    Represents INP `pted` elements.
    """

    _KEYWORD = 'pted'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.Integer, 'Edits by fine mesh on/off', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1})

    _REGEX = re.compile(rf'\Apted( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
