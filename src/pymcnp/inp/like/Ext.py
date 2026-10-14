import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Ext(_field.Fields, _option.LikeOption):
    """
    Represents INP `ext` elements.
    """

    _KEYWORD = 'ext'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    designator = _field.Field(types.Designator, 'Gets `designator`', required=True, numeric=())
    stretch = _field.Field(types.String, 'Gets `stretch`', required=True, numeric=())

    _REGEX = re.compile(rf'\Aext:(\S+)( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
