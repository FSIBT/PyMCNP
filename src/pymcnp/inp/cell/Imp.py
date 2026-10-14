import re

from .. import _field
from . import _option
from ... import types


class Imp(_field.Fields, _option.CellOption):
    """
    Represents INP `imp` elements.
    """

    _KEYWORD = 'imp'

    designator = _field.Field(types.Designator, 'Data option particle designator', required=True, numeric=())
    importance = _field.Field(types.Real, 'Cell particle importance', required=True)

    _REGEX = re.compile(rf'\Aimp:(\S+)( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
