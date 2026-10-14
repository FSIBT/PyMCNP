import re

from .. import _field
from . import _option
from ... import types


class Iu(_field.Fields, _option.DfOption_1):
    """
    Represents INP `iu` elements.
    """

    _KEYWORD = 'iu'

    units = _field.Field(types.Integer, 'Control units', required=True, numeric=int, invalid=lambda self, value: not (isinstance(value.value, types.Jump) or value in {1, 2}))

    _REGEX = re.compile(rf'\Aiu( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
