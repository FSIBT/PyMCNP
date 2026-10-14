import re

from .. import _field
from . import _option
from ... import types


class Nps(_field.Fields, _option.StopOption):
    """
    Represents INP `nps` elements.
    """

    _KEYWORD = 'nps'

    npp = _field.Field(types.Integer, 'Total number of histories before stop', required=True, numeric=int)
    npsmg = _field.Field(types.Integer, 'Number of histories before stop', numeric=int)

    _REGEX = re.compile(rf'\Anps( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)
