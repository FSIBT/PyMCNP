import re

from ... import _field
from . import _option
from .... import types


class Diffsol(_field.Fields, _option.BlockOption):
    """
    Represents INP `diffsol` elements.
    """

    _KEYWORD = 'diffsol'

    setting = _field.Field(types.String, 'Diffusion operator solver', required=True, numeric=())

    _REGEX = re.compile(rf'\Adiffsol( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
