import re

from .. import _field
from . import _option
from ... import types


class Cell(_field.Fields, _option.KpertOption):
    """
    Represents INP `cell` elements.
    """

    _KEYWORD = 'cell'

    numbers = _field.Field.tuple(types.Integer, 'List of cells', required=True, numeric=int)

    _REGEX = re.compile(rf'\Acell((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
