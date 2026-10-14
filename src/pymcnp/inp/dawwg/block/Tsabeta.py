import re

from ... import _field
from . import _option
from .... import types


class Tsabeta(_field.Fields, _option.BlockOption):
    """
    Represents INP `tsabeta` elements.
    """

    _KEYWORD = 'tsabeta'

    setting = _field.Field(types.Real, 'Scattering cross-section reduction for TSA', required=True)

    _REGEX = re.compile(rf'\Atsabeta( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
