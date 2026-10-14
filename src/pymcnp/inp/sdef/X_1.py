import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class X_1(_field.Fields, _option.SdefOption):
    """
    Represents INP `x` elements variation #1.
    """

    _KEYWORD = 'x'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    position = _field.Field(types.Distribution, 'Position x-component', required=True, numeric=())

    _REGEX = re.compile(rf'\Ax( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
