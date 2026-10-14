import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Time(_field.Fields, _option.EmbeeOption):
    """
    Represents INP `time` elements.
    """

    _KEYWORD = 'time'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    factor = _field.Field(types.Real, 'Multiplicative conversion factor for time-related output', required=True, invalid=lambda self, value: not value > 0)

    _REGEX = re.compile(rf'\Atime( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
