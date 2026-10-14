import re

from ... import _field
from . import _option
from .... import types


class Noedtt(_field.Fields, _option.BlockOption):
    """
    Represents INP `noedtt` elements.
    """

    _KEYWORD = 'noedtt'

    setting = _field.Field(types.Integer, 'Suppress writing EDITIT on/off', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1})

    _REGEX = re.compile(rf'\Anoedtt( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
