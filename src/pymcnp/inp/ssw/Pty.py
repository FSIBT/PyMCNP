import re

from .. import _field
from . import _option
from ... import types


class Pty(_field.Fields, _option.SswOption):
    """
    Represents INP `pty` elements.
    """

    _KEYWORD = 'pty'

    tracks = _field.Field.tuple(types.Designator, 'Tracks to record', required=True, numeric=())

    _REGEX = re.compile(rf'\Apty((?: {types.Designator._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
