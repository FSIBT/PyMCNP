import re

from ... import _field
from . import _option
from .... import types


class Isn(_field.Fields, _option.BlockOption):
    """
    Represents INP `isn` elements.
    """

    _KEYWORD = 'isn'

    setting = _field.Field(types.Integer, 'Sn order', required=True, numeric=int)

    _REGEX = re.compile(rf'\Aisn( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
