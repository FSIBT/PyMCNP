import re

from .. import _field
from . import _option
from ... import types


class Hlib(_field.Fields, _option.MOption_0):
    """
    Represents INP `hlib` elements.
    """

    _KEYWORD = 'hlib'

    abx = _field.Field(types.String, 'Default proton table identifier', required=True, numeric=())

    _REGEX = re.compile(rf'\Ahlib( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
