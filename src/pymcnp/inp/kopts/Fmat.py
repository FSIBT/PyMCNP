import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Fmat(_field.Fields, _option.KoptsOption):
    """
    Represents INP `fmat` elements.
    """

    _KEYWORD = 'fmat'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.String, 'Yes/No FMAT', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'yes', 'no'})

    _REGEX = re.compile(rf'\Afmat( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
