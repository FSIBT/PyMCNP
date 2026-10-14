import re

from .. import _field
from . import _option
from ... import types


class Legendre(_field.Fields, _option.KsenOption):
    """
    Represents INP `legendre` elements.
    """

    _KEYWORD = 'legendre'

    number = _field.Field(types.Integer, 'Order of Legendre moments to calculate sensitivities', required=True, numeric=int)

    _REGEX = re.compile(rf'\Alegendre( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
