import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Cofi(_field.Fields, _option.TOption_1):
    """
    Represents INP `cofi` elements.
    """

    _KEYWORD = 'cofi'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    time = _field.Field(types.Real, 'Dead time interval', required=True)

    _REGEX = re.compile(rf'\Acofi( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
