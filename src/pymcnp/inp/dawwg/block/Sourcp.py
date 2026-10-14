import re

from ... import _field
from . import _option
from .... import types
from .... import errors


class Sourcp(_field.Fields, _option.BlockOption):
    """
    Represents INP `sourcp` elements.
    """

    _KEYWORD = 'sourcp'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.Integer, 'Source print flag', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1, 2, 3})

    _REGEX = re.compile(rf'\Asourcp( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
