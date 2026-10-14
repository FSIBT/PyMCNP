import re

from ... import _field
from . import _option
from .... import types
from .... import errors


class Angp(_field.Fields, _option.BlockOption):
    """
    Represents INP `angp` elements.
    """

    _KEYWORD = 'angp'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.Integer, 'Print angular flux on/off', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1})

    _REGEX = re.compile(rf'\Aangp( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
