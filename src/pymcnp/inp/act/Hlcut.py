import re

from .. import _field
from . import _option
from ... import types


class Hlcut(_field.Fields, _option.ActOption):
    """
    Represents INP `hlcut` elements.
    """

    _KEYWORD = 'hlcut'

    cutoff = _field.Field(types.Real, 'Spontaneous-decay half-life threshold', required=True)

    _REGEX = re.compile(rf'\Ahlcut( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
