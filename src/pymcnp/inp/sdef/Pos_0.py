import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Pos_0(_field.Fields, _option.SdefOption):
    """
    Represents INP `pos` elements variation #0.
    """

    _KEYWORD = 'pos'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    x = _field.Field(types.Real, 'Position sampling x-coordinate', required=True)
    y = _field.Field(types.Real, 'Position sampling y-coordinate', required=True)
    z = _field.Field(types.Real, 'Position sampling z-coordinate', required=True)

    _REGEX = re.compile(rf'\Apos( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
