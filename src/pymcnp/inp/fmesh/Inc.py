import re

from .. import _field
from . import _option
from ... import types


class Inc(_field.Fields, _option.FmeshOption):
    """
    Represents INP `inc` elements.
    """

    _KEYWORD = 'inc'

    lower = _field.Field(types.Real, 'Collision for FMESH tally lower bound', required=True)
    upper = _field.Field(types.Real, 'Collision for FMESH tally upper bound')

    _REGEX = re.compile(rf'\Ainc( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)
