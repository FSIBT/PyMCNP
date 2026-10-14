import re

from .. import _field
from . import _option
from ... import types


class Kints(_field.Fields, _option.MeshOption):
    """
    Represents INP `kints` elements.
    """

    _KEYWORD = 'kints'

    number = _field.Field.tuple(types.Integer, 'Number of fine meshes within corresponding coarse meshes in the z/theta directions', required=True, numeric=int)

    _REGEX = re.compile(rf'\Akints((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
