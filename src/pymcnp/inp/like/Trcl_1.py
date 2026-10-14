import re

from .. import _field
from . import _option
from ... import types


class Trcl_1(_field.Fields, _option.LikeOption):
    """
    Represents INP `trcl` elements variation #1.
    """

    _KEYWORD = 'trcl'

    _ORDER = ('transformation', 'prefix')

    prefix = _field.Field(types.String, 'Gets `prefix`', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'*'})
    transformation = _field.Field(types.Transformation_0, 'Gets `transformation`', required=True, numeric=())

    _REGEX = re.compile(rf'\A([*])?trcl( {types.Transformation_0._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
