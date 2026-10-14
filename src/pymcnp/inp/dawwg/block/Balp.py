import re

from ... import _field
from . import _option
from .... import types
from .... import errors


class Balp(_field.Fields, _option.BlockOption):
    """
    Represents INP `balp` elements.
    """

    _KEYWORD = 'balp'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.Integer, 'Print coarse-mesh balance tables on/off', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1})

    _REGEX = re.compile(rf'\Abalp( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
