import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Dump(_field.Fields, _option.MplotOption):
    """
    Represents INP `dump` elements.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD

    _KEYWORD = 'dump'

    n = _field.Field(types.Integer, 'RUNTPE read dump number', numeric=int)

    _REGEX = re.compile(rf'\Adump( {types.Integer._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)
