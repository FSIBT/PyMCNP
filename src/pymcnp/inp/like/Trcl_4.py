import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Trcl_4(_field.Fields, _option.LikeOption):
    """
    Represents INP `trcl` elements variation #4.
    """

    _KEYWORD = 'trcl'

    _CODE = errors.InpCode.SEMANTICS_OPTION
    _ORDER = ('transformation', 'prefix')

    prefix = _field.Field(types.String, 'Gets `prefix`', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'*'})
    transformation = _field.Field(types.Transformation_3, 'Gets `transformation`', required=True, numeric=())

    _REGEX = re.compile(rf'\A([*])?trcl( {types.Transformation_3._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
