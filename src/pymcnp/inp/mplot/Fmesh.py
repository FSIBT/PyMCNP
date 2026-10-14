import re

from .. import _field
from . import _option
from ... import types


class Fmesh(_field.Fields, _option.MplotOption):
    """
    Represents INP `fmesh` elements.
    """

    _KEYWORD = 'fmesh'

    n = _field.Field(types.Integer, 'Tally to plot', required=True, numeric=int)

    _REGEX = re.compile(rf'\Afmesh( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
