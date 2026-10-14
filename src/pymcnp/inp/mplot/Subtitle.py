import re

from .. import _field
from . import _option
from ... import types


class Subtitle(_field.Fields, _option.MplotOption):
    """
    Represents INP `subtitle` elements.
    """

    _KEYWORD = 'subtitle'

    x = _field.Field(types.Integer, 'X-coordinate of location', required=True, numeric=int)
    y = _field.Field(types.Integer, 'Y-coordinate of location', required=True, numeric=int)
    aa = _field.Field(types.String, 'Line to substitute', required=True, numeric=(), invalid=lambda self, value: not len(value) <= 40)

    _REGEX = re.compile(rf'\Asubtitle( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})( \"{types.String._REGEX.pattern[2:-2]}\")\Z', re.IGNORECASE)
