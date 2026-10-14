import re

from ... import _field
from . import _option
from .... import types


class Ftr(_field.Fields, _option.FOption):
    """
    Represents INP `ftr` elements.
    """

    _KEYWORD = 'ftr'

    distribution = _field.Field(types.Distribution, 'Dependent distribution', required=True, numeric=())

    _REGEX = re.compile(rf'\Aftr( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
