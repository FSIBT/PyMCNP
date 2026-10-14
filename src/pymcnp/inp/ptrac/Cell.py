import re

from .. import _field
from . import _option
from ... import types


class Cell(_field.Fields, _option.PtracOption):
    """
    Represents INP `cell` elements.
    """

    _KEYWORD = 'cell'

    numbers = _field.Field.tuple(types.Integer, 'List of cell numbers for filtering', required=True, numeric=int)

    _REGEX = re.compile(rf'\Acell((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
