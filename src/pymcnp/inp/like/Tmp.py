import re

from .. import _field
from . import _option
from ... import types


class Tmp(_field.Fields, _option.LikeOption):
    """
    Represents INP `tmp` elements.
    """

    _KEYWORD = 'tmp'

    _ORDER = ('temperature', 'suffix')

    suffix = _field.Field(types.Integer, 'Gets `suffix`', numeric=int)
    temperature = _field.Field.tuple(types.Real, 'Gets `temperature`', required=True, invalid=lambda self, value: not min(value) > 0)

    _REGEX = re.compile(rf'\Atmp(\d+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
