import re

from ... import _field
from . import _option
from .... import types
from .... import errors


class Ibr(_field.Fields, _option.BlockOption):
    """
    Represents INP `ibr` elements.
    """

    _KEYWORD = 'ibr'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.Integer, 'Right boudary condition', required=True, numeric=int)

    _REGEX = re.compile(rf'\Aibr( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
