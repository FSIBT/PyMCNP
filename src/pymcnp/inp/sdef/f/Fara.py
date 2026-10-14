import re

from ... import _field
from . import _option
from .... import types


class Fara(_field.Fields, _option.FOption):
    """
    Represents INP `fara` elements.
    """

    _KEYWORD = 'fara'

    distribution = _field.Field(types.Distribution, 'Dependent distribution', required=True, numeric=())

    _REGEX = re.compile(rf'\Afara( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
