import re

from .. import _field
from . import _option
from ... import types


class Nreact(_field.Fields, _option.TroptOption):
    """
    Represents INP `nreact` elements.
    """

    _KEYWORD = 'nreact'

    setting = _field.Field(types.String, 'Nuclear reactions setting', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'off', 'on', 'atten', 'remove'})

    _REGEX = re.compile(rf'\Anreact( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
