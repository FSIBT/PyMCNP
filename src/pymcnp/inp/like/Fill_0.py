import re

from .. import _field
from . import _option
from ... import types


class Fill_0(_field.Fields, _option.LikeOption):
    """
    Represents INP `fill` elements variation #0.
    """

    _KEYWORD = 'fill'

    _ORDER = ('i', 'j', 'k', 'universes', 'prefix', 'm')

    prefix = _field.Field(types.String, 'Gets `prefix`', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'*'})
    i = _field.Field(types.Index, 'Gets `i`', required=True, numeric=())
    j = _field.Field(types.Index, 'Gets `j`', required=True, numeric=())
    k = _field.Field(types.Index, 'Gets `k`', required=True, numeric=())
    universes = _field.Field.tuple(types.Integer, 'Gets `universes`', required=True, numeric=int)
    m = _field.Field(types.Integer, 'Gets `m`', numeric=int)

    _REGEX = re.compile(rf'\A([*])?fill (\S+:\S+) (\S+:\S+) (\S+:\S+)((?: {types.Integer._REGEX.pattern[2:-2]})+?)(?: [(]({types.Integer._REGEX.pattern[2:-2]})[)])?\Z', re.IGNORECASE)
