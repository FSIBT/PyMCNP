import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Jmesh(_field.Fields, _option.MeshOption):
    """
    Represents INP `jmesh` elements.
    """

    _KEYWORD = 'jmesh'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    vector = _field.Field.tuple(types.Real, 'Locations of the coarse meshes in the y/z directions', required=True)

    _REGEX = re.compile(rf'\Ajmesh((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
