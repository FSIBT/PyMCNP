import re

from ... import _field
from . import _option
from .... import types


class Lib(_field.Fields, _option.BlockOption):
    """
    Represents INP `lib` elements.
    """

    _KEYWORD = 'lib'

    setting = _field.Field(types.String, 'Name of cross-section file', required=True, numeric=())

    _REGEX = re.compile(rf'\Alib( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
