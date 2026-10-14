import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Fac(_field.Fields, _option.DfOption_1):
    """
    Represents INP `fac` elements.
    """

    _KEYWORD = 'fac'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    normalization = _field.Field(types.Integer, 'Normalization factor for dose', required=True, numeric=int, invalid=lambda self, value: not (isinstance(value.value, types.Jump) or value >= -3))

    _REGEX = re.compile(rf'\Afac( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
