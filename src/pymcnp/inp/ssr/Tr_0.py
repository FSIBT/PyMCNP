import re

from .. import _field
from . import _option
from ... import types


class Tr_0(_field.Fields, _option.SsrOption):
    """
    Represents INP `tr` elements variation #0.
    """

    _KEYWORD = 'tr'

    number = _field.Field(types.Distribution, 'Particle weight', required=True, numeric=())

    _REGEX = re.compile(rf'\Atr( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
