import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Coni(_field.Fields, _option.TOption_1):
    """
    Represents INP `coni` elements.
    """

    _KEYWORD = 'coni'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    time = _field.Field(types.Real, 'Alive time interval', required=True)

    _REGEX = re.compile(rf'\Aconi( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
