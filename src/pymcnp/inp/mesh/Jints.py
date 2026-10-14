import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Jints(_field.Fields, _option.MeshOption):
    """
    Represents INP `jints` elements.
    """

    _KEYWORD = 'jints'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    number = _field.Field.tuple(types.Integer, 'Number of fine meshes within corresponding coarse meshes in the y/z directions', required=True, numeric=int)

    _REGEX = re.compile(rf'\Ajints((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
