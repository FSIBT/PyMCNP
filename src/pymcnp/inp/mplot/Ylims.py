import re

from .. import _field
from . import _option
from ... import types


class Ylims(_field.Fields, _option.MplotOption):
    """
    Represents INP `ylims` elements.
    """

    _KEYWORD = 'ylims'

    lower = _field.Field(types.Real, 'Y-axis lower limit', required=True)
    upper = _field.Field(types.Real, 'Y-axis upper limit', required=True, invalid=lambda self, value: not self.lower < value)
    nsteps = _field.Field(types.Real, 'Y-axis interval', invalid=lambda self, value: value is not None and (not value >= 0))

    _REGEX = re.compile(rf'\Aylims( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)
