import re

from .. import _field
from . import _option
from ... import types


class Tmesh(_field.Fields, _option.FmeshOption):
    """
    Represents INP `tmesh` elements.
    """

    _KEYWORD = 'tmesh'

    time = _field.Field(types.Real, 'Values of mesh points in time', required=True)

    _REGEX = re.compile(rf'\Atmesh( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
