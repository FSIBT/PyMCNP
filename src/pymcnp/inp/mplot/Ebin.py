import re

from .. import _field
from . import _option
from ... import types


class Ebin(_field.Fields, _option.MplotOption):
    """
    Represents INP `ebin` elements.
    """

    _KEYWORD = 'ebin'

    n = _field.Field(types.Integer, 'Energy bin to plot', required=True, numeric=int)

    _REGEX = re.compile(rf'\Aebin( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
