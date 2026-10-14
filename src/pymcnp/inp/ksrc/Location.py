import re

from .. import _field
from . import _entry
from ... import types
from ... import errors


class Location(_field.Fields, _entry.KsrcEntry):
    """
    Represents INP `location` elements.
    """

    _KEYWORD = ''

    _CODE = errors.InpCode.SEMANTICS_OPTION

    x = _field.Field(types.Real, 'Location x-coordinate', required=True)
    y = _field.Field(types.Real, 'Location y-coordinate', required=True)
    z = _field.Field(types.Real, 'Location z-coordinate', required=True)

    _REGEX = re.compile(rf'\A({types.Real._REGEX.pattern[2:-2]}) ({types.Real._REGEX.pattern[2:-2]}) ({types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
