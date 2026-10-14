import re

from .. import _field
from . import _option
from ... import types


class Hist(_field.Fields, _option.RandOption):
    """
    Represents INP `hist` elements.
    """

    _KEYWORD = 'hist'

    hist = _field.Field(types.Integer, 'Starting pseudorandom number', required=True, numeric=int)

    _REGEX = re.compile(rf'\Ahist( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
