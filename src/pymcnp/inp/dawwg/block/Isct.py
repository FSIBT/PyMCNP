import re

from ... import _field
from . import _option
from .... import types


class Isct(_field.Fields, _option.BlockOption):
    """
    Represents INP `isct` elements.
    """

    _KEYWORD = 'isct'

    setting = _field.Field(types.Integer, 'Legendre order', required=True, numeric=int)

    _REGEX = re.compile(rf'\Aisct( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
