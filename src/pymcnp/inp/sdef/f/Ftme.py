import re

from ... import _field
from . import _option
from .... import types


class Ftme(_field.Fields, _option.FOption):
    """
    Represents INP `ftme` elements.
    """

    _KEYWORD = 'ftme'

    distribution = _field.Field(types.Distribution, 'Dependent distribution', required=True, numeric=())

    _REGEX = re.compile(rf'\Aftme( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
