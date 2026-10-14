import re

from .. import _field
from . import _option
from ... import types


class Fcl(_field.Fields, _option.LikeOption):
    """
    Represents INP `fcl` elements.
    """

    _KEYWORD = 'fcl'

    designator = _field.Field(types.Designator, 'Gets `designator`', required=True, numeric=())
    control = _field.Field(types.Real, 'Gets `control`', required=True, invalid=lambda self, value: not (value >= -1 and value <= 1))

    _REGEX = re.compile(rf'\Afcl:(\S+)( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
