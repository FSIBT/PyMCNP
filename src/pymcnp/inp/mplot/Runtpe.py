import re

from .. import _field
from . import _option
from ... import types


class Runtpe(_field.Fields, _option.MplotOption):
    """
    Represents INP `runtpe` elements.
    """

    _KEYWORD = 'runtpe'

    filename = _field.Field(types.String, 'RUNTPE file to read dump', required=True, numeric=())
    n = _field.Field(types.Integer, 'RUNTPE read dump number', numeric=int)

    _REGEX = re.compile(rf'\Aruntpe( {types.String._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)
