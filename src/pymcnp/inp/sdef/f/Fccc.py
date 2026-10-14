import re

from ... import _field
from . import _option
from .... import types


class Fccc(_field.Fields, _option.FOption):
    """
    Represents INP `fccc` elements.
    """

    _KEYWORD = 'fccc'

    distribution = _field.Field(types.Distribution, 'Dependent distribution', required=True, numeric=())

    _REGEX = re.compile(rf'\Afccc( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
