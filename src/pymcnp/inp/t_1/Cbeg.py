import re

from .. import _field
from . import _option
from ... import types


class Cbeg(_field.Fields, _option.TOption_1):
    """
    Represents INP `cbeg` elements.
    """

    _KEYWORD = 'cbeg'

    time = _field.Field(types.Real, 'Reference starting time', required=True)

    _REGEX = re.compile(rf'\Acbeg( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
