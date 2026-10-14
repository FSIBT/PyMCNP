import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Seed(_field.Fields, _option.RandOption):
    """
    Represents INP `seed` elements.
    """

    _KEYWORD = 'seed'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    seed = _field.Field(types.Integer, 'Random number generator seed', required=True, numeric=int, invalid=lambda self, value: not value % 2 == 1)

    _REGEX = re.compile(rf'\Aseed( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
