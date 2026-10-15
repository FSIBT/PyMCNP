import re

from .. import _field
from . import _option
from ... import types


class Dxc(_field.Fields, _option.CellOption):
    """
    Represents INP `dxc` elements.
    """

    _KEYWORD = 'dxc'

    _ORDER = ('designator', 'probability', 'suffix')

    suffix = _field.Field(types.Integer, 'Cell option suffix', numeric=int)
    designator = _field.Field(types.Designator, 'Cell particle designator', required=True, numeric=())
    probability = _field.Field(types.Real, 'Cell probability of DXTRAN contribution', required=True, invalid=lambda self, value: not (value >= 0 and value <= 1))

    _REGEX = re.compile(rf'\Adxc(\d*):(\S+)( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
