import re

from .. import _field
from . import _option
from ... import types


class Elpt(_field.Fields, _option.LikeOption):
    """
    Represents INP `elpt` elements.
    """

    _KEYWORD = 'elpt'

    designator = _field.Field(types.Designator, 'Gets `designator`', required=True, numeric=())
    cutoff = _field.Field(types.Real, 'Gets `cutoff`', required=True)

    _REGEX = re.compile(rf'\Aelpt:(\S+)( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
