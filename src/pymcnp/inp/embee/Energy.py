import re

from .. import _field
from . import _option
from ... import types


class Energy(_field.Fields, _option.EmbeeOption):
    """
    Represents INP `energy` elements.
    """

    _KEYWORD = 'energy'

    factor = _field.Field(types.Real, 'Multiplicative conversion factor for energy-related output', required=True, invalid=lambda self, value: not value > 0)

    _REGEX = re.compile(rf'\Aenergy( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
