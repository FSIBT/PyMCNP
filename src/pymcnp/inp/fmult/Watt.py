import re

from .. import _field
from . import _option
from ... import types


class Watt(_field.Fields, _option.FmultOption):
    """
    Represents INP `watt` elements.
    """

    _KEYWORD = 'watt'

    a = _field.Field(types.Real, 'Watt energy spectrum parameters a', required=True)
    b = _field.Field(types.Real, 'Watt energy spectrum parameters b', required=True)

    _REGEX = re.compile(rf'\Awatt( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
