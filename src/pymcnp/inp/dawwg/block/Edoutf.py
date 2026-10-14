import re

from ... import _field
from . import _option
from .... import types
from .... import errors


class Edoutf(_field.Fields, _option.BlockOption):
    """
    Represents INP `edoutf` elements.
    """

    _KEYWORD = 'edoutf'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.Integer, 'ASCII output files control', required=True, numeric=int, invalid=lambda self, value: value not in {-3, -2, -1, 0, 1, 2, 3})

    _REGEX = re.compile(rf'\Aedoutf( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
