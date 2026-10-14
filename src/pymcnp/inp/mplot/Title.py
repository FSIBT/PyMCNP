import re

from .. import _field
from . import _option
from ... import types


class Title(_field.Fields, _option.MplotOption):
    """
    Represents INP `title` elements.
    """

    _KEYWORD = 'title'

    n = _field.Field(types.Integer, 'Line number', required=True, numeric=int, invalid=lambda self, value: not value > 0)
    aa = _field.Field(types.String, 'Line to substitute', required=True, numeric=(), invalid=lambda self, value: not len(value) <= 40)

    _REGEX = re.compile(rf'\Atitle( {types.Integer._REGEX.pattern[2:-2]})( \"{types.String._REGEX.pattern[2:-2]}\")\Z', re.IGNORECASE)
