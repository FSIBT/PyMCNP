import re

from ... import _field
from . import _option
from .... import types


class Srcacc(_field.Fields, _option.BlockOption):
    """
    Represents INP `srcacc` elements.
    """

    _KEYWORD = 'srcacc'

    setting = _field.Field(types.String, 'Transport accelerations', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'dsa', 'tsa', 'no'})

    _REGEX = re.compile(rf'\Asrcacc( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
