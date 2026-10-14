import re

from .. import _field
from . import _option
from ... import types


class Erg_1(_field.Fields, _option.SdefOption):
    """
    Represents INP `erg` elements variation #1.
    """

    _KEYWORD = 'erg'

    energy = _field.Field(types.Distribution, 'Kinetic energy', required=True, numeric=())

    _REGEX = re.compile(rf'\Aerg( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
