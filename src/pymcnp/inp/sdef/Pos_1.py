import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Pos_1(_field.Fields, _option.SdefOption):
    """
    Represents INP `pos` elements variation #1.
    """

    _KEYWORD = 'pos'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    vector = _field.Field(types.Distribution, 'Position sampling vector-coordinate', required=True, numeric=())

    _REGEX = re.compile(rf'\Apos( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
