import re

from .. import _field
from . import _option
from ... import types


class Nescat(_field.Fields, _option.TroptOption):
    """
    Represents INP `nescat` elements.
    """

    _KEYWORD = 'nescat'

    setting = _field.Field(types.String, 'Nuclear elastic scattering setting', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'off', 'on'})

    _REGEX = re.compile(rf'\Anescat( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
