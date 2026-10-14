import re

from .. import _field
from . import _option
from ... import types


class Tr_1(_field.Fields, _option.SdefOption):
    """
    Represents INP `tr` elements variation #1.
    """

    _KEYWORD = 'tr'

    number = _field.Field(types.Distribution, 'Particle weight', required=True, numeric=())

    _REGEX = re.compile(rf'\Atr( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
