import re

from .. import _field
from . import _option
from ... import types


class Legend(_field.Fields, _option.MplotOption):
    """
    Represents INP `legend` elements.
    """

    _KEYWORD = 'legend'

    x = _field.Field(types.Real, 'Label x-location')
    y = _field.Field(types.Real, 'Label x-location')

    _REGEX = re.compile(rf'\Alegend( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)
