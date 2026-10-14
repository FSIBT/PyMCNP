import re

from ... import _field
from . import _option
from .... import types


class Fx(_field.Fields, _option.FOption):
    """
    Represents INP `fx` elements.
    """

    _KEYWORD = 'fx'

    distribution = _field.Field(types.Distribution, 'Dependent distribution', required=True, numeric=())

    _REGEX = re.compile(rf'\Afx( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
