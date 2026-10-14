import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Method(_field.Fields, _option.FmultOption):
    """
    Represents INP `method` elements.
    """

    _KEYWORD = 'method'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.Integer, 'Gaussian sampling algorithm setting', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1, 3, 5, 6, 7})

    _REGEX = re.compile(rf'\Amethod( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
