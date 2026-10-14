import re

from .. import _field
from . import _option
from ... import types


class Embed(_field.Fields, _option.EmbeeOption):
    """
    Represents INP `embed` elements.
    """

    _KEYWORD = 'embed'

    number = _field.Field(types.Integer, 'Embedded mesh universe number', required=True, numeric=int, invalid=lambda self, value: not (value >= 0 and value <= 99999999))

    _REGEX = re.compile(rf'\Aembed( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
