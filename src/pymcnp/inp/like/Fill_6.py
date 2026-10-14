import re

from .. import _field
from . import _option
from ... import types


class Fill_6(_field.Fields, _option.LikeOption):
    """
    Represents INP `fill` elements variation #6.
    """

    _KEYWORD = 'fill'

    _ORDER = ('universe', 'prefix', 'transformation')

    prefix = _field.Field(types.String, 'Gets `prefix`', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'*'})
    universe = _field.Field(types.Integer, 'Gets `universe`', required=True, numeric=int, invalid=lambda self, value: not (value == 10000000000 or (value >= 0 and value <= 99999999)))
    transformation = _field.Field(types.Integer, 'Gets `transformation`', numeric=int, invalid=lambda self, value: value is not None and (not (value >= 0 and value <= 999)))

    _REGEX = re.compile(rf'\A([*])?fill( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]}| [(]{types.Integer._REGEX.pattern[2:-2]}[)])?\Z', re.IGNORECASE)
