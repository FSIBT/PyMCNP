import re

from .. import _field
from . import _option
from ... import types


class Cel(_field.Fields, _option.SswOption):
    """
    Represents INP `cel` elements.
    """

    _KEYWORD = 'cel'

    cfs = _field.Field.tuple(types.Integer, 'Cells from which KCODE neutrons are written', required=True, numeric=int)

    _REGEX = re.compile(rf'\Acel((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
