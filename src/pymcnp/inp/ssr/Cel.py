import re

from .. import _field
from . import _option
from ... import types


class Cel(_field.Fields, _option.SsrOption):
    """
    Represents INP `cel` elements.
    """

    _KEYWORD = 'cel'

    numbers = _field.Field.tuple(types.Integer, 'Tuple of cell from subset of cells on SSW card', required=True, numeric=int)

    _REGEX = re.compile(rf'\Acel((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
