import re

from ... import _field
from . import _option
from .... import types


class Rzmflux(_field.Fields, _option.BlockOption):
    """
    Represents INP `rzmflux` elements.
    """

    _KEYWORD = 'rzmflux'

    setting = _field.Field(types.Integer, 'Write b-flux file on/off', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1})

    _REGEX = re.compile(rf'\Arzmflux( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
