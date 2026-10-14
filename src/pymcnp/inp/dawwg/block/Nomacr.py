import re

from ... import _field
from . import _option
from .... import types


class Nomacr(_field.Fields, _option.BlockOption):
    """
    Represents INP `nomacr` elements.
    """

    _KEYWORD = 'nomacr'

    setting = _field.Field(types.Integer, 'Suppress writing MACRXS on/off', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1})

    _REGEX = re.compile(rf'\Anomacr( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
