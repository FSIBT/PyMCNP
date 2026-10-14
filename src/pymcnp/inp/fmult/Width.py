import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Width(_field.Fields, _option.FmultOption):
    """
    Represents INP `width` elements.
    """

    _KEYWORD = 'width'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    width = _field.Field(types.Real, 'Width for sampling spontaneous fission', required=True)

    _REGEX = re.compile(rf'\Awidth( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
