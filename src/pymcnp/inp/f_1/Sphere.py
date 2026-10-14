import re

from .. import _field
from . import _entry
from ... import types


class Sphere(_field.Fields, _entry.FEntry_1):
    """
    Represents INP `sphere` elements.
    """

    _KEYWORD = ''

    x = _field.Field(types.Real, 'Vector x coordinate', required=True)
    y = _field.Field(types.Real, 'Vector y coordinate', required=True)
    z = _field.Field(types.Real, 'Vector z coordinate', required=True)
    ro = _field.Field(types.Real, 'Sphere exclusion radius', required=True)

    _REGEX = re.compile(rf'\A({types.Real._REGEX.pattern[2:-2]}) ({types.Real._REGEX.pattern[2:-2]}) ({types.Real._REGEX.pattern[2:-2]}) ({types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
