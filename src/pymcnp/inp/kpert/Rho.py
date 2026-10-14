import re

from .. import _field
from . import _option
from ... import types


class Rho(_field.Fields, _option.KpertOption):
    """
    Represents INP `rho` elements.
    """

    _KEYWORD = 'rho'

    densities = _field.Field.tuple(types.Real, 'List of densities', required=True)

    _REGEX = re.compile(rf'\Arho((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
