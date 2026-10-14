import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Pd(_field.Fields, _option.CellOption):
    """
    Represents INP `pd` elements.
    """

    _KEYWORD = 'pd'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    suffix = _field.Field(types.Integer, 'Cell option suffix', required=True, numeric=int)
    probability = _field.Field(types.Real, 'Cell probability of DXTRAN contribution', required=True, invalid=lambda self, value: not (value >= 0 and value <= 1))

    _REGEX = re.compile(rf'\Apd(\d+)( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
