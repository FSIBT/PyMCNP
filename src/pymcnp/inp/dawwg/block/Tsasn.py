import re

from ... import _field
from . import _option
from .... import types


class Tsasn(_field.Fields, _option.BlockOption):
    """
    Represents INP `tsasn` elements.
    """

    _KEYWORD = 'tsasn'

    setting = _field.Field(types.Integer, 'Sn order for lower order TSA sweeps', required=True, numeric=int)

    _REGEX = re.compile(rf'\Atsasn( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
