import re

from .. import _field
from . import block
from . import _option
from ... import types
from ... import errors


class Block(_field.Fields, _option.DawwgOption):
    """
    Represents INP `block` elements.
    """

    _KEYWORD = 'block'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.Integer, 'Destination of key-value pairs', required=True, numeric=int, invalid=lambda self, value: value not in {1, 3, 5, 6})
    options = _field.Field.tuple(block.BlockOption, 'Dictionary of options', numeric=())

    _REGEX = re.compile(rf'\Ablock( {types.Integer._REGEX.pattern[2:-2]})((?: (?:{block.BlockOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)
