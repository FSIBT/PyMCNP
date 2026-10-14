import re

from ... import _field
from . import _option
from .... import types


class Byvolp(_field.Fields, _option.BlockOption):
    """
    Represents INP `byvolp` elements.
    """

    _KEYWORD = 'byvolp'

    setting = _field.Field(types.Integer, 'Printed point reactions rates on/off', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1})

    _REGEX = re.compile(rf'\Abyvolp( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
