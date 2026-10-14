import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Tal(_field.Fields, _option.MplotOption):
    """
    Represents INP `tal` elements.
    """

    _KEYWORD = 'tal'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    n = _field.Field(types.Integer, 'Tally number', required=True, numeric=int)

    _REGEX = re.compile(rf'\Atal( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
