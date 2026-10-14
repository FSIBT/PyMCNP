import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Wwn(_field.Fields, _option.LikeOption):
    """
    Represents INP `wwn` elements.
    """

    _KEYWORD = 'wwn'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    suffix = _field.Field(types.Integer, 'Gets `suffix`', required=True, numeric=int)
    designator = _field.Field(types.Designator, 'Gets `designator`', required=True, numeric=())
    bound = _field.Field(types.Real, 'Gets `bound`', required=True, invalid=lambda self, value: not (value == -1 or value >= 0))

    _REGEX = re.compile(rf'\Awwn(\d+):(\S+)( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
