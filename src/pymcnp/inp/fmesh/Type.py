import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Type(_field.Fields, _option.FmeshOption):
    """
    Represents INP `type` elements.
    """

    _KEYWORD = 'type'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.String, 'Tally quantity', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'flux', 'source'})

    _REGEX = re.compile(rf'\Atype( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
