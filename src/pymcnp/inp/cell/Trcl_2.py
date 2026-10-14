import re

from .. import _field
from . import _option
from ... import types


class Trcl_2(_field.Fields, _option.CellOption):
    """
    Represents INP `trcl` elements variation #2.
    """

    _KEYWORD = 'trcl'

    _ORDER = ('transformation', 'prefix')

    prefix = _field.Field(types.String, 'Star prefix', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'*'})
    transformation = _field.Field(types.Transformation_1, 'Cell transformation', required=True, numeric=())

    _REGEX = re.compile(rf'\A([*])?trcl( {types.Transformation_1._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
