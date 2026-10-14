import re

from .. import _field
from . import _option
from ... import types


class Tr_1(_field.Fields, _option.SsrOption):
    """
    Represents INP `tr` elements variation #1.
    """

    _KEYWORD = 'tr'

    number = _field.Field(types.Integer, 'Particle weight', required=True, numeric=int)

    _REGEX = re.compile(rf'\Atr( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
