import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Surface(_field.Fields, _option.PtracOption):
    """
    Represents INP `surface` elements.
    """

    _KEYWORD = 'surface'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    numbers = _field.Field.tuple(types.Integer, 'List of surface numbers for filtering', required=True, numeric=int)

    _REGEX = re.compile(rf'\Asurface((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
