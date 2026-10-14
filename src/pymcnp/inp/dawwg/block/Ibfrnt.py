import re

from ... import _field
from . import _option
from .... import types


class Ibfrnt(_field.Fields, _option.BlockOption):
    """
    Represents INP `ibfrnt` elements.
    """

    _KEYWORD = 'ibfrnt'

    setting = _field.Field(types.Integer, 'Front boudary condition', required=True, numeric=int)

    _REGEX = re.compile(rf'\Aibfrnt( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
