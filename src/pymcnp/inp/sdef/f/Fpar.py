import re

from ... import _field
from . import _option
from .... import types


class Fpar(_field.Fields, _option.FOption):
    """
    Represents INP `fpar` elements.
    """

    _KEYWORD = 'fpar'

    distribution = _field.Field(types.Distribution, 'Dependent distribution', required=True, numeric=())

    _REGEX = re.compile(rf'\Afpar( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
