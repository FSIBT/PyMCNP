import re

from .. import _field
from . import _option
from ... import types


class Ext(_field.Fields, _option.SsrOption):
    """
    Represents INP `ext` elements.
    """

    _KEYWORD = 'ext'

    number = _field.Field(types.Distribution, 'Distribution number for baising sampling', required=True, numeric=())

    _REGEX = re.compile(rf'\Aext( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
