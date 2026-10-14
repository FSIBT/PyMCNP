import re

from .. import _field
from . import _option
from ... import types


class Term(_field.Fields, _option.MplotOption):
    """
    Represents INP `term` elements.
    """

    _KEYWORD = 'term'

    n = _field.Field(types.Integer, 'Output decive specifier', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1})

    _REGEX = re.compile(rf'\Aterm( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
