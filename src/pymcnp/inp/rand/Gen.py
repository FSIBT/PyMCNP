import re

from .. import _field
from . import _option
from ... import types


class Gen(_field.Fields, _option.RandOption):
    """
    Represents INP `gen` elements.
    """

    _KEYWORD = 'gen'

    setting = _field.Field(types.Integer, 'Type of pseudorandom number generator', required=True, numeric=int, invalid=lambda self, value: value not in {1, 2, 3, 4})

    _REGEX = re.compile(rf'\Agen( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
