import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Data(_field.Fields, _option.FmultOption):
    """
    Represents INP `data` elements.
    """

    _KEYWORD = 'data'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.Integer, 'Sampling method setting', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1, 2, 3})

    _REGEX = re.compile(rf'\Adata( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
