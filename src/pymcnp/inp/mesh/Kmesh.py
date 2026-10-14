import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Kmesh(_field.Fields, _option.MeshOption):
    """
    Represents INP `kmesh` elements.
    """

    _KEYWORD = 'kmesh'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    vector = _field.Field.tuple(types.Real, 'Locations of the coarse meshes in the z/theta directions', required=True)

    _REGEX = re.compile(rf'\Akmesh((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
