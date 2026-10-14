import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Dir_1(_field.Fields, _option.SdefOption):
    """
    Represents INP `dir` elements variation #1.
    """

    _KEYWORD = 'dir'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    cosine = _field.Field(types.Distribution, 'Cosine of the angle between VEC and particle', required=True, numeric=())

    _REGEX = re.compile(rf'\Adir( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
