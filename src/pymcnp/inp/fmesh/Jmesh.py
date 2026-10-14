import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Jmesh(_field.Fields, _option.FmeshOption):
    """
    Represents INP `jmesh` elements.
    """

    _KEYWORD = 'jmesh'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    locations = _field.Field.tuple(types.Real, 'Locations of mesh points y/z for rectangular/cylindrical geometry', required=True)

    _REGEX = re.compile(rf'\Ajmesh((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
