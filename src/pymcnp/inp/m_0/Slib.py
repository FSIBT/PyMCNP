import re

from .. import _field
from . import _option
from ... import types


class Slib(_field.Fields, _option.MOption_0):
    """
    Represents INP `slib` elements.
    """

    _KEYWORD = 'slib'

    abx = _field.Field(types.String, 'Default helion table identifier', required=True, numeric=())

    _REGEX = re.compile(rf'\Aslib( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
