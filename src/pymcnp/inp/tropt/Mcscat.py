import re

from .. import _field
from . import _option
from ... import types


class Mcscat(_field.Fields, _option.TroptOption):
    """
    Represents INP `mcscat` elements.
    """

    _KEYWORD = 'mcscat'

    setting = _field.Field(types.String, 'Multiple coulomb scattering setting', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'off', 'fnal1', 'gaussian', 'fnal2'})

    _REGEX = re.compile(rf'\Amcscat( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
