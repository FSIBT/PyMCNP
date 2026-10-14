import re

from .. import _field
from . import _option
from ... import types


class Tally(_field.Fields, _option.MplotOption):
    """
    Represents INP `tally` elements.
    """

    _KEYWORD = 'tally'

    n = _field.Field(types.Integer, 'Number of current tally', numeric=int)

    _REGEX = re.compile(rf'\Atally( {types.Integer._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)
