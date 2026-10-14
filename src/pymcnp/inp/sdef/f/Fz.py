import re

from ... import _field
from . import _option
from .... import types


class Fz(_field.Fields, _option.FOption):
    """
    Represents INP `fz` elements.
    """

    _KEYWORD = 'fz'

    distribution = _field.Field(types.Distribution, 'Dependent distribution', required=True, numeric=())

    _REGEX = re.compile(rf'\Afz( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
