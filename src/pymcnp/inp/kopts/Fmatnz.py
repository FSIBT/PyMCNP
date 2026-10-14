import re

from .. import _field
from . import _option
from ... import types


class Fmatnz(_field.Fields, _option.KoptsOption):
    """
    Represents INP `fmatnz` elements.
    """

    _KEYWORD = 'fmatnz'

    fmat_nz = _field.Field(types.Real, 'Fmat_nz', required=True)

    _REGEX = re.compile(rf'\Afmatnz( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
