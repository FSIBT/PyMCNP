import re

from .. import _field
from . import _option
from ... import types


class Elib(_field.Fields, _option.MOption_0):
    """
    Represents INP `elib` elements.
    """

    _KEYWORD = 'elib'

    abx = _field.Field(types.String, 'Default electron table identifier', required=True, numeric=())

    _REGEX = re.compile(rf'\Aelib( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
