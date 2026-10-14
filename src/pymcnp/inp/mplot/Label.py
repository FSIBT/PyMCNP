import re

from .. import _field
from . import _option
from ... import types


class Label(_field.Fields, _option.MplotOption):
    """
    Represents INP `label` elements.
    """

    _KEYWORD = 'label'

    aa = _field.Field(types.String, 'Line to substitute', required=True, numeric=(), invalid=lambda self, value: not len(value) <= 10)

    _REGEX = re.compile(rf'\Alabel( \"{types.String._REGEX.pattern[2:-2]}\")\Z', re.IGNORECASE)
