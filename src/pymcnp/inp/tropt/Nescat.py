import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Nescat(_field.Fields, _option.TroptOption):
    """
    Represents INP `nescat` elements.
    """

    _KEYWORD = 'nescat'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.String, 'Nuclear elastic scattering setting', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'off', 'on'})

    _REGEX = re.compile(rf'\Anescat( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
