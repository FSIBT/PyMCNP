import re

from .. import _field
from . import _option
from ... import types


class File(_field.Fields, _option.MplotOption):
    """
    Represents INP `file` elements.
    """

    _KEYWORD = 'file'

    aa = _field.Field(types.String, 'Graphics metafile on/off', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'all', 'none'})

    _REGEX = re.compile(r'\Afile(?: (all|none))?\Z', re.IGNORECASE)
