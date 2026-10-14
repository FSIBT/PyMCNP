import re

from .. import _field
from . import _option
from ... import types


class Constrain(_field.Fields, _option.KsenOption):
    """
    Represents INP `constrain` elements.
    """

    _KEYWORD = 'constrain'

    setting = _field.Field(types.String, 'Renormalize sensitivity distribution on/off', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'yes', 'no'})

    _REGEX = re.compile(rf'\Aconstrain( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
