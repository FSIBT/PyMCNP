import re

from .. import _field
from . import _option
from ... import types


class Ic(_field.Fields, _option.DfOption_1):
    """
    Represents INP `ic` elements.
    """

    _KEYWORD = 'ic'

    function = _field.Field(
        types.Integer, 'Standard dose function', required=True, numeric=int, invalid=lambda self, value: not (isinstance(value.value, types.Jump) or value in {10, 20, 31, 32, 33, 34, 35, 40, 99})
    )

    _REGEX = re.compile(rf'\Aic( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
