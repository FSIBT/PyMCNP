import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Cell(_field.Fields, _option.PertOption):
    """
    Represents INP `cell` elements.
    """

    _KEYWORD = 'cell'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    numbers = _field.Field.tuple(types.Integer, 'List of cells', required=True, numeric=int)

    _REGEX = re.compile(rf'\Acell((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
