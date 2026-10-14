import re

from ... import _field
from . import _option
from .... import types


class Astop(_field.Fields, _option.BlockOption):
    """
    Represents INP `astop` elements.
    """

    _KEYWORD = 'astop'

    setting = _field.Field(types.Integer, 'Bottom-going flux at plane j', required=True, numeric=int)

    _REGEX = re.compile(rf'\Aastop( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
