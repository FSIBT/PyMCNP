import re

from .. import _field
from . import _option
from ... import types


class Dlib(_field.Fields, _option.MOption_0):
    """
    Represents INP `dlib` elements.
    """

    _KEYWORD = 'dlib'

    abx = _field.Field(types.String, 'Default deuteron table identifier', required=True, numeric=())

    _REGEX = re.compile(rf'\Adlib( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
