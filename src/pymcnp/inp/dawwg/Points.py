import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Points(_field.Fields, _option.DawwgOption):
    """
    Represents INP `points` elements.
    """

    _KEYWORD = 'points'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    count = _field.Field(types.Integer, 'Number of sample points for each direction in each mesh', required=True, numeric=int)

    _REGEX = re.compile(rf'\Apoints( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
