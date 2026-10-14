import re

from .. import _field
from . import _option
from ... import types


class Imesh(_field.Fields, _option.MeshOption):
    """
    Represents INP `imesh` elements.
    """

    _KEYWORD = 'imesh'

    vector = _field.Field.tuple(types.Real, 'Locations of the coarse meshes in the x/r directions', required=True)

    _REGEX = re.compile(rf'\Aimesh((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
