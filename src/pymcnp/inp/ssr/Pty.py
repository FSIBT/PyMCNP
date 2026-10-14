import re

from .. import _field
from . import _option
from ... import types


class Pty(_field.Fields, _option.SsrOption):
    """
    Represents INP `pty` elements.
    """

    _KEYWORD = 'pty'

    particles = _field.Field.tuple(types.Designator, 'Tuple of designators', required=True, numeric=())

    _REGEX = re.compile(rf'\Apty((?: {types.Designator._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
