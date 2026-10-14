import re

from ... import _field
from . import _option
from .... import types


class Ibl(_field.Fields, _option.BlockOption):
    """
    Represents INP `ibl` elements.
    """

    _KEYWORD = 'ibl'

    setting = _field.Field(types.Integer, 'Left boundary condition', required=True, numeric=int)

    _REGEX = re.compile(rf'\Aibl( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
