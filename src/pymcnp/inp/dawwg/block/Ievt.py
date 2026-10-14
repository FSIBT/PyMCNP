import re

from ... import _field
from . import _option
from .... import types
from .... import errors


class Ievt(_field.Fields, _option.BlockOption):
    """
    Represents INP `ievt` elements.
    """

    _KEYWORD = 'ievt'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.Integer, 'Calculation type', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1, 2, 3, 4})

    _REGEX = re.compile(rf'\Aievt( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
