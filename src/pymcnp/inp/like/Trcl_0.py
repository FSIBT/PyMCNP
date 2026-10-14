import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Trcl_0(_field.Fields, _option.LikeOption):
    """
    Represents INP `trcl` elements variation #0.
    """

    _KEYWORD = 'trcl'

    _CODE = errors.InpCode.SEMANTICS_OPTION
    _ORDER = ('transformation', 'prefix')

    prefix = _field.Field(types.String, 'Gets `prefix`', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'*'})
    transformation = _field.Field(types.Integer, 'Gets `transformation`', required=True, numeric=int, invalid=lambda self, value: not (value >= 0 and value <= 999))

    _REGEX = re.compile(rf'\A([*])?trcl( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
