import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Vec(_field.Fields, _option.BfldOption):
    """
    Represents INP `vec` elements.
    """

    _KEYWORD = 'vec'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    vector = _field.Field.tuple(types.Real, 'Direction of mangentic field or plane corresponding to the x-axis of the quadrapole', required=True)

    _REGEX = re.compile(rf'\Avec((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
