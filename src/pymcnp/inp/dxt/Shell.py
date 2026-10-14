import re

from .. import _field
from . import _entry
from ... import types
from ... import errors


class Shell(_field.Fields, _entry.DxtEntry):
    """
    Represents INP `shell` elements.
    """

    _KEYWORD = ''

    _CODE = errors.InpCode.SEMANTICS_OPTION

    x = _field.Field(types.Real, 'Vector x coordinate', required=True)
    y = _field.Field(types.Real, 'Vector y coordinate', required=True)
    z = _field.Field(types.Real, 'Vector z coordinate', required=True)
    inner_radius = _field.Field(types.Integer, 'Inner sphere radius', required=True, numeric=int)
    outer_radius = _field.Field(types.Integer, 'Outer sphere radius', required=True, numeric=int)

    _REGEX = re.compile(
        rf'\A({types.Real._REGEX.pattern[2:-2]}) ({types.Real._REGEX.pattern[2:-2]}) ({types.Real._REGEX.pattern[2:-2]}) ({types.Integer._REGEX.pattern[2:-2]}) ({types.Integer._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )
