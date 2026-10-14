import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Refs(_field.Fields, _option.MOption_0):
    """
    Represents INP `refs` elements.
    """

    _KEYWORD = 'refs'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    coefficents = _field.Field.tuple(types.Real, 'Sellmeier coefficents', required=True)

    _REGEX = re.compile(rf'\Arefs((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
