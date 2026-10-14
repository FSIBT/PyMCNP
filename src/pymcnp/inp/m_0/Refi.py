import re

from .. import _field
from . import _option
from ... import types


class Refi(_field.Fields, _option.MOption_0):
    """
    Represents INP `refi` elements.
    """

    _KEYWORD = 'refi'

    refractive_index = _field.Field(types.Real, 'Refractive index constant', required=True)

    _REGEX = re.compile(rf'\Arefi( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
