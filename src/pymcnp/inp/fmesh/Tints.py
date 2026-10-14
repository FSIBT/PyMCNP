import re

from .. import _field
from . import _option
from ... import types


class Tints(_field.Fields, _option.FmeshOption):
    """
    Represents INP `tints` elements.
    """

    _KEYWORD = 'tints'

    count = _field.Field(types.Integer, 'Number of mesh points for each mesh time', required=True, numeric=int)

    _REGEX = re.compile(rf'\Atints( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
