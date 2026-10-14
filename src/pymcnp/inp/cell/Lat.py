import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Lat(_field.Fields, _option.CellOption):
    """
    Represents INP `lat` elements.
    """

    _KEYWORD = 'lat'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    shape = _field.Field(types.Integer, 'Cell lattice shape', required=True, numeric=int, invalid=lambda self, value: value not in {1, 2})

    _REGEX = re.compile(rf'\Alat( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
