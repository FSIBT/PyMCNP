import re

from ... import _field
from . import _option
from .... import types


class Noasg(_field.Fields, _option.BlockOption):
    """
    Represents INP `noasg` elements.
    """

    _KEYWORD = 'noasg'

    setting = _field.Field(types.Integer, 'Suppress writing ASGMAT on/off', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1})

    _REGEX = re.compile(rf'\Anoasg( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
