import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Cfrq(_field.Fields, _option.TOption_1):
    """
    Represents INP `cfrq` elements.
    """

    _KEYWORD = 'cfrq'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    frequency = _field.Field(types.Real, 'Frequency of cycling', required=True)

    _REGEX = re.compile(rf'\Acfrq( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
