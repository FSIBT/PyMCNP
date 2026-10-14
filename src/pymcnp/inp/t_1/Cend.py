import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Cend(_field.Fields, _option.TOption_1):
    """
    Represents INP `cend` elements.
    """

    _KEYWORD = 'cend'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    time = _field.Field(types.Real, 'Reference ending time', required=True)

    _REGEX = re.compile(rf'\Acend( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
