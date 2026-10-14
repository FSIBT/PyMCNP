import re

from ... import _field
from . import _option
from .... import types


class Fcel(_field.Fields, _option.FOption):
    """
    Represents INP `fcel` elements.
    """

    _KEYWORD = 'fcel'

    distribution = _field.Field(types.Distribution, 'Dependent distribution', required=True, numeric=())

    _REGEX = re.compile(rf'\Afcel( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
