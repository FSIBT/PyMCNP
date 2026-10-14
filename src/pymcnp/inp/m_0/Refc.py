import re

from .. import _field
from . import _option
from ... import types


class Refc(_field.Fields, _option.MOption_0):
    """
    Represents INP `refc` elements.
    """

    _KEYWORD = 'refc'

    coefficents = _field.Field.tuple(types.Real, 'Cauchy coefficents', required=True)

    _REGEX = re.compile(rf'\Arefc((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
