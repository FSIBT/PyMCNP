import re

from ... import _field
from . import _option
from .... import types


class Ibback(_field.Fields, _option.BlockOption):
    """
    Represents INP `ibback` elements.
    """

    _KEYWORD = 'ibback'

    setting = _field.Field(types.Integer, 'Back boudary condition', required=True, numeric=int)

    _REGEX = re.compile(rf'\Aibback( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
