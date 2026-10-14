import re

from .. import _field
from . import _option
from ... import types


class Iints(_field.Fields, _option.MeshOption):
    """
    Represents INP `iints` elements.
    """

    _KEYWORD = 'iints'

    number = _field.Field.tuple(types.Integer, 'Number of fine meshes within corresponding coarse meshes in the x/r directions', required=True, numeric=int)

    _REGEX = re.compile(rf'\Aiints((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
