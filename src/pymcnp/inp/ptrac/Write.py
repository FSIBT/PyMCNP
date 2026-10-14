import re

from .. import _field
from . import _option
from ... import types


class Write(_field.Fields, _option.PtracOption):
    """
    Represents INP `write` elements.
    """

    _KEYWORD = 'write'

    setting = _field.Field(types.String, 'Controls what particle parameters are written', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'pos', 'all'})

    _REGEX = re.compile(r'\Awrite(?: (pos|all))\Z', re.IGNORECASE)
