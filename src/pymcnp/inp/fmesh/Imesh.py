import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Imesh(_field.Fields, _option.FmeshOption):
    """
    Represents INP `imesh` elements.
    """

    _KEYWORD = 'imesh'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    locations = _field.Field.tuple(types.Real, 'Locations of mesh points x/r for rectangular/cylindrical geometry', required=True)

    _REGEX = re.compile(rf'\Aimesh((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
