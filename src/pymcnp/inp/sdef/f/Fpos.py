import re

from ... import _field
from . import _option
from .... import types


class Fpos(_field.Fields, _option.FOption):
    """
    Represents INP `fpos` elements.
    """

    _KEYWORD = 'fpos'

    distribution = _field.Field(types.Distribution, 'Dependent distribution', required=True, numeric=())

    _REGEX = re.compile(rf'\Afpos( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
