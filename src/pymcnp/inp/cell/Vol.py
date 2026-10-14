import re

from .. import _field
from . import _option
from ... import types


class Vol(_field.Fields, _option.CellOption):
    """
    Represents INP `vol` elements.
    """

    _KEYWORD = 'vol'

    volume = _field.Field(types.Real, 'Cell volume', required=True, invalid=lambda self, value: not value >= 0)

    _REGEX = re.compile(rf'\Avol( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
