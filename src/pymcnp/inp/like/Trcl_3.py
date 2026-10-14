import re

from .. import _field
from . import _option
from ... import types


class Trcl_3(_field.Fields, _option.LikeOption):
    """
    Represents INP `trcl` elements variation #3.
    """

    _KEYWORD = 'trcl'

    _ORDER = ('transformation', 'prefix')

    prefix = _field.Field(types.String, 'Gets `prefix`', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'*'})
    transformation = _field.Field(types.Transformation_2, 'Gets `transformation`', required=True, numeric=())

    _REGEX = re.compile(rf'\A([*])?trcl( {types.Transformation_2._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
