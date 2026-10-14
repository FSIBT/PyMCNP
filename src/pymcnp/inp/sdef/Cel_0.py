import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Cel_0(_field.Fields, _option.SdefOption):
    """
    Represents INP `cel` elements variation #0.
    """

    _KEYWORD = 'cel'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    number = _field.Field(types.Integer, 'Cell number', required=True, numeric=int, invalid=lambda self, value: not (isinstance(value.value, types.Jump) or (value >= 0 and value <= 99999999)))

    _REGEX = re.compile(rf'\Acel( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
