import re

from .. import _field
from . import _option
from ... import types


class Ext(_field.Fields, _option.CellOption):
    """
    Represents INP `ext` elements.
    """

    _KEYWORD = 'ext'

    designator = _field.Field(types.Designator, 'Cell particle designator', required=True, numeric=())
    stretch = _field.Field(types.String, 'Cell exponential transform stretching specifier', required=True, numeric=())

    _REGEX = re.compile(rf'\Aext:(\S+)( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
