import re

from ... import _field
from . import _option
from .... import types


class Nosolv(_field.Fields, _option.BlockOption):
    """
    Represents INP `nosolv` elements.
    """

    _KEYWORD = 'nosolv'

    setting = _field.Field(types.Integer, 'Suppress solver module on/off', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1})

    _REGEX = re.compile(rf'\Anosolv( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
