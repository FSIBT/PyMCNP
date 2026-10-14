import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class File(_field.Fields, _option.PtracOption):
    """
    Represents INP `file` elements.
    """

    _KEYWORD = 'file'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.String, 'PTRAC file type', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'asc', 'bin', 'aov', 'bov'})

    _REGEX = re.compile(r'\Afile(?: (asc|bin|aov|bov))\Z', re.IGNORECASE)
