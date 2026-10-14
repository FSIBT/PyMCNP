import re

from .. import _field
from . import _option
from ... import types


class Stride(_field.Fields, _option.RandOption):
    """
    Represents INP `stride` elements.
    """

    _KEYWORD = 'stride'

    stride = _field.Field(types.Integer, 'Number of random numbers between source particle', required=True, numeric=int)

    _REGEX = re.compile(rf'\Astride( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
