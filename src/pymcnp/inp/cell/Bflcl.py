import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Bflcl(_field.Fields, _option.CellOption):
    """
    Represents INP `bflcl` elements.
    """

    _KEYWORD = 'bflcl'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    number = _field.Field(types.Integer, 'Cell magnetic field number', required=True, numeric=int, invalid=lambda self, value: not value >= 0)

    _REGEX = re.compile(rf'\Abflcl( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
