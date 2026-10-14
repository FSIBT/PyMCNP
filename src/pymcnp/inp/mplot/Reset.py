import re

from .. import _field
from . import _option
from ... import types


class Reset(_field.Fields, _option.MplotOption):
    """
    Represents INP `reset` elements.
    """

    _KEYWORD = 'reset'

    aa = _field.Field(types.String, 'Command parameter reset', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'all', 'coplot'})

    _REGEX = re.compile(r'\Areset(?: (all|coplot))?\Z', re.IGNORECASE)
