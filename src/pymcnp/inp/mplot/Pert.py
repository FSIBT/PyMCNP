import re

from .. import _field
from . import _option
from ... import types


class Pert(_field.Fields, _option.MplotOption):
    """
    Represents INP `pert` elements.
    """

    _KEYWORD = 'pert'

    n = _field.Field(types.Integer, 'Number on a PERT card', numeric=int)

    _REGEX = re.compile(rf'\Apert( {types.Integer._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)
