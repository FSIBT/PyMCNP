import re

from .. import _field
from . import _option
from ... import types


class Ytitle(_field.Fields, _option.MplotOption):
    """
    Represents INP `ytitle` elements.
    """

    _KEYWORD = 'ytitle'

    aa = _field.Field(types.String, 'Line to substitute', required=True, numeric=(), invalid=lambda self, value: not len(value) <= 40)

    _REGEX = re.compile(rf'\Aytitle( \"{types.String._REGEX.pattern[2:-2]}\")\Z', re.IGNORECASE)
