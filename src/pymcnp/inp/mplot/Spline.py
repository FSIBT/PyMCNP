import re

from .. import _field
from . import _option
from ... import types


class Spline(_field.Fields, _option.MplotOption):
    """
    Represents INP `spline` elements.
    """

    _KEYWORD = 'spline'

    x = _field.Field(types.Real, 'Tension of rational splines')

    _REGEX = re.compile(rf'\Aspline( {types.Real._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)
