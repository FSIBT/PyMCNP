import re

from .. import _field
from . import _option
from ... import types


class Wwn(_field.Fields, _option.CellOption):
    """
    Represents INP `wwn` elements.
    """

    _KEYWORD = 'wwn'

    suffix = _field.Field(types.Integer, 'Cell option suffix', required=True, numeric=int)
    designator = _field.Field(types.Designator, 'Cell particle designator', required=True, numeric=())
    bound = _field.Field(types.Real, 'Cell weight-window space, time, or energy lower bound', required=True, invalid=lambda self, value: not (value == -1 or value >= 0))

    _REGEX = re.compile(rf'\Awwn(\d+):(\S+)( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
