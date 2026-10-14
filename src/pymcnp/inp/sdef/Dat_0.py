import re

from .. import _field
from . import _option
from ... import types


class Dat_0(_field.Fields, _option.SdefOption):
    """
    Represents INP `dat` elements variation #0.
    """

    _KEYWORD = 'dat'

    month = _field.Field(types.Integer, 'Month for cosmic-ray & background sources', required=True, numeric=int, invalid=lambda self, value: not (value >= 1 and value <= 12))
    day = _field.Field(types.Integer, 'Day for cosmic-ray & background sources', required=True, numeric=int, invalid=lambda self, value: not (value >= 1 and value <= 31))
    year = _field.Field(types.Integer, 'Year for cosmic-ray & background sources', required=True, numeric=int, invalid=lambda self, value: not (value >= 1 and value <= 9999))

    _REGEX = re.compile(rf'\Adat( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
