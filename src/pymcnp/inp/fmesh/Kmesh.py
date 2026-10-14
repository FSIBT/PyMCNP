import re

from .. import _field
from . import _option
from ... import types


class Kmesh(_field.Fields, _option.FmeshOption):
    """
    Represents INP `kmesh` elements.
    """

    _KEYWORD = 'kmesh'

    locations = _field.Field.tuple(types.Real, 'Locations of mesh points z/theta for rectangular/cylindrical geometry', required=True)

    _REGEX = re.compile(rf'\Akmesh((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
