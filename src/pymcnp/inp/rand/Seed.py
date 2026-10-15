import re

from .. import _field
from . import _option
from ... import types


class Seed(_field.Fields, _option.RandOption):
    """
    Represents INP `seed` elements.
    """

    _KEYWORD = 'seed'

    seed = _field.Field(types.Integer, 'Random number generator seed', required=True, numeric=int, invalid=lambda self, value: value % 2 != 1)

    _REGEX = re.compile(rf'\Aseed( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
