import re

from .. import _field
from . import _option
from ... import types


class Eloss(_field.Fields, _option.TroptOption):
    """
    Represents INP `eloss` elements.
    """

    _KEYWORD = 'eloss'

    setting = _field.Field(types.String, 'Slowing down energy losses setting', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'off', 'strag1', 'csda'})

    _REGEX = re.compile(rf'\Aeloss( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
