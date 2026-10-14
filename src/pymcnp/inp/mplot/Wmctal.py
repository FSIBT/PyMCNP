import re

from .. import _field
from . import _option
from ... import types


class Wmctal(_field.Fields, _option.MplotOption):
    """
    Represents INP `wmctal` elements.
    """

    _KEYWORD = 'wmctal'

    filename = _field.Field(types.String, 'MCTAL file to write', required=True, numeric=())

    _REGEX = re.compile(rf'\Awmctal( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
