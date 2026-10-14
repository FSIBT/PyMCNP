import re

from .. import _field
from . import _option
from ... import types


class Tal(_field.Fields, _option.MplotOption):
    """
    Represents INP `tal` elements.
    """

    _KEYWORD = 'tal'

    n = _field.Field(types.Integer, 'Tally number', required=True, numeric=int)

    _REGEX = re.compile(rf'\Atal( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
