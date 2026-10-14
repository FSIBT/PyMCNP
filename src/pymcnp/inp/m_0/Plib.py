import re

from .. import _field
from . import _option
from ... import types


class Plib(_field.Fields, _option.MOption_0):
    """
    Represents INP `plib` elements.
    """

    _KEYWORD = 'plib'

    abx = _field.Field(types.String, 'Default photoatomic table identifier', required=True, numeric=())

    _REGEX = re.compile(rf'\Aplib( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
