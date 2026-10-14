import re

from ... import _field
from . import _option
from .... import types


class Noedit(_field.Fields, _option.BlockOption):
    """
    Represents INP `noedit` elements.
    """

    _KEYWORD = 'noedit'

    setting = _field.Field(types.Integer, 'Suppress edit module on/off', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1})

    _REGEX = re.compile(rf'\Anoedit( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
