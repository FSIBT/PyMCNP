import re

from .. import _field
from . import _option
from ... import types


class Eints(_field.Fields, _option.FmeshOption):
    """
    Represents INP `eints` elements.
    """

    _KEYWORD = 'eints'

    count = _field.Field(types.Integer, 'Number of mesh points for each mesh energy', required=True, numeric=int)

    _REGEX = re.compile(rf'\Aeints( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
