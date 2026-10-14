import re

from ... import _field
from . import _option
from .... import types


class Fissrp(_field.Fields, _option.BlockOption):
    """
    Represents INP `fissrp` elements.
    """

    _KEYWORD = 'fissrp'

    setting = _field.Field(types.Integer, 'Print fission source rate on/off', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1})

    _REGEX = re.compile(rf'\Afissrp( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
