import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Bcw(_field.Fields, _option.SsrOption):
    """
    Represents INP `bcw` elements.
    """

    _KEYWORD = 'bcw'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    radius = _field.Field(types.Real, 'Radius of cylindrical window', required=True)
    zb = _field.Field(types.Real, 'Bottom of cylindrical window', required=True, invalid=lambda self, value: not value > 0)
    ze = _field.Field(types.Real, 'Top of cylindrical window', required=True, invalid=lambda self, value: not (self.zb > 0 and self.zb < value))

    _REGEX = re.compile(rf'\Abcw( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
