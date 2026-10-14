import re

from ... import _field
from . import _option
from .... import types
from .... import errors


class Trcor(_field.Fields, _option.BlockOption):
    """
    Represents INP `trcor` elements.
    """

    _KEYWORD = 'trcor'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.String, 'Trcor', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'diag'})

    _REGEX = re.compile(rf'\Atrcor( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
