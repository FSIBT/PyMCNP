import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class X_0(_field.Fields, _option.SdefOption):
    """
    Represents INP `x` elements variation #0.
    """

    _KEYWORD = 'x'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    position = _field.Field(types.Real, 'Position x-component', required=True)

    _REGEX = re.compile(rf'\Ax( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
