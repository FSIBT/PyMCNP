import re

from ... import _field
from . import _option
from .... import types


class Ferg(_field.Fields, _option.FOption):
    """
    Represents INP `ferg` elements.
    """

    _KEYWORD = 'ferg'

    distribution = _field.Field(types.Distribution, 'Dependent distribution', required=True, numeric=())

    _REGEX = re.compile(rf'\Aferg( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
