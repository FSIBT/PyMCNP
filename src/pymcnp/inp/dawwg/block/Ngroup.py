import re

from ... import _field
from . import _option
from .... import types


class Ngroup(_field.Fields, _option.BlockOption):
    """
    Represents INP `ngroup` elements.
    """

    _KEYWORD = 'ngroup'

    value = _field.Field(types.Integer, 'Number of energy groups', required=True, numeric=int)

    _REGEX = re.compile(rf'\Angroup( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
