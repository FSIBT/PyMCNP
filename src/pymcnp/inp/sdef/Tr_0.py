import re

from .. import _field
from . import _option
from ... import types


class Tr_0(_field.Fields, _option.SdefOption):
    """
    Represents INP `tr` elements variation #0.
    """

    _KEYWORD = 'tr'

    number = _field.Field(types.Integer, 'Particle weight', required=True, numeric=int)

    _REGEX = re.compile(rf'\Atr( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
