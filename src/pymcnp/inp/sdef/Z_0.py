import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Z_0(_field.Fields, _option.SdefOption):
    """
    Represents INP `z` elements variation #0.
    """

    _KEYWORD = 'z'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    position = _field.Field(types.Real, 'Position z-component', required=True)

    _REGEX = re.compile(rf'\Az( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
