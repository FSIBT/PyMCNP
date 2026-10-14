import re

from .. import _field
from . import _option
from ... import types


class Blocksize(_field.Fields, _option.KoptsOption):
    """
    Represents INP `blocksize` elements.
    """

    _KEYWORD = 'blocksize'

    ncy = _field.Field(types.Integer, 'Number of cycles in every outer iteration', required=True, numeric=int, invalid=lambda self, value: not value >= 2)

    _REGEX = re.compile(rf'\Ablocksize( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
