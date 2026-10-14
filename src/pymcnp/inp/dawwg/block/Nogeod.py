import re

from ... import _field
from . import _option
from .... import types


class Nogeod(_field.Fields, _option.BlockOption):
    """
    Represents INP `nogeod` elements.
    """

    _KEYWORD = 'nogeod'

    setting = _field.Field(types.Integer, 'Suppress writing GEODST on/off', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1})

    _REGEX = re.compile(rf'\Anogeod( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
