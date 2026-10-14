import re

from .. import _field
from . import _option
from ... import types


class Dxc(_field.Fields, _option.LikeOption):
    """
    Represents INP `dxc` elements.
    """

    _KEYWORD = 'dxc'

    suffix = _field.Field(types.Integer, 'Gets `suffix`', required=True, numeric=int)
    designator = _field.Field(types.Designator, 'Gets `designator`', required=True, numeric=())
    probability = _field.Field(types.Real, 'Gets `probability`', required=True, invalid=lambda self, value: not (value >= 0 and value <= 1))

    _REGEX = re.compile(rf'\Adxc(\d+):(\S+)( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
