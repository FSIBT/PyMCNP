import re

from .. import _field
from . import _option
from ... import types


class Surface(_field.Fields, _option.PtracOption):
    """
    Represents INP `surface` elements.
    """

    _KEYWORD = 'surface'

    numbers = _field.Field.tuple(types.Integer, 'List of surface numbers for filtering', required=True, numeric=int)

    _REGEX = re.compile(rf'\Asurface((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
