import re

from .. import _field
from . import _option
from ... import types


class Meph(_field.Fields, _option.PtracOption):
    """
    Represents INP `meph` elements.
    """

    _KEYWORD = 'meph'

    events = _field.Field(types.Integer, 'Maximum number of events per history to write', required=True, numeric=int, invalid=lambda self, value: not value > 0)

    _REGEX = re.compile(rf'\Ameph( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
