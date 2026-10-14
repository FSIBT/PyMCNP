import re

from ... import _field
from . import _option
from .... import types


class Asbott(_field.Fields, _option.BlockOption):
    """
    Represents INP `asbott` elements.
    """

    _KEYWORD = 'asbott'

    setting = _field.Field(types.Integer, 'Top-going flux at plane j', required=True, numeric=int)

    _REGEX = re.compile(rf'\Aasbott( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
