import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Fill_5(_field.Fields, _option.LikeOption):
    """
    Represents INP `fill` elements variation #5.
    """

    _KEYWORD = 'fill'

    _CODE = errors.InpCode.SEMANTICS_OPTION
    _ORDER = ('universe', 'prefix', 'transformation')

    prefix = _field.Field(types.String, 'Gets `prefix`', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'*'})
    universe = _field.Field(types.Integer, 'Gets `universe`', required=True, numeric=int, invalid=lambda self, value: not (value == 10000000000 or (value >= 0 and value <= 99999999)))
    transformation = _field.Field(types.Transformation_4, 'Gets `transformation`', numeric=())

    _REGEX = re.compile(rf'\A([*])?fill( {types.Integer._REGEX.pattern[2:-2]})( {types.Transformation_4._REGEX.pattern[2:-2]}| [(]{types.Transformation_4._REGEX.pattern[2:-2]}[)])?\Z', re.IGNORECASE)
