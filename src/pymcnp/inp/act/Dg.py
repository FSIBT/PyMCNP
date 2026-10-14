import re

from .. import _field
from . import _option
from ... import types


class Dg(_field.Fields, _option.ActOption):
    """
    Represents INP `dg` elements.
    """

    _KEYWORD = 'dg'

    source = _field.Field(types.String, 'Delayed gamma data source', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'line', 'mg', 'none'})

    _REGEX = re.compile(rf'\Adg( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
