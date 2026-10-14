import re

from ... import _field
from . import _option
from .... import types


class Nomix(_field.Fields, _option.BlockOption):
    """
    Represents INP `nomix` elements.
    """

    _KEYWORD = 'nomix'

    setting = _field.Field(types.Integer, 'Suppress writing mixing on/off', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1})

    _REGEX = re.compile(rf'\Anomix( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
