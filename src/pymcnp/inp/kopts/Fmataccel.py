import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Fmataccel(_field.Fields, _option.KoptsOption):
    """
    Represents INP `fmataccel` elements.
    """

    _KEYWORD = 'fmataccel'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.String, 'Fmataccel', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'yes', 'no'})

    _REGEX = re.compile(rf'\Afmataccel( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
