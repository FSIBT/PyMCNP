import re

from .. import _field
from . import _option
from ... import types


class Cel_1(_field.Fields, _option.SdefOption):
    """
    Represents INP `cel` elements variation #1.
    """

    _KEYWORD = 'cel'

    number = _field.Field(types.Distribution, 'Cell number', required=True, numeric=())

    _REGEX = re.compile(rf'\Acel( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
