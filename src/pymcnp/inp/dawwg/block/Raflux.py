import re

from ... import _field
from . import _option
from .... import types


class Raflux(_field.Fields, _option.BlockOption):
    """
    Represents INP `raflux` elements.
    """

    _KEYWORD = 'raflux'

    setting = _field.Field(types.Integer, 'Prepare angular flux file on/off', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1})

    _REGEX = re.compile(rf'\Araflux( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
