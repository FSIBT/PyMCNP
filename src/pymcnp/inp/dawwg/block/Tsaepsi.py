import re

from ... import _field
from . import _option
from .... import types


class Tsaepsi(_field.Fields, _option.BlockOption):
    """
    Represents INP `tsaepsi` elements.
    """

    _KEYWORD = 'tsaepsi'

    setting = _field.Field(types.Real, 'Convergence criteria for TSA sweeps', required=True)

    _REGEX = re.compile(rf'\Atsaepsi( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
