import re

from .. import _field
from . import _option
from ... import types


class Pause(_field.Fields, _option.MplotOption):
    """
    Represents INP `pause` elements.
    """

    _KEYWORD = 'pause'

    n = _field.Field(types.Integer, 'Pause duration', numeric=int)

    _REGEX = re.compile(rf'\Apause( {types.Integer._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)
