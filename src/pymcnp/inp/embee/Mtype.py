import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Mtype(_field.Fields, _option.EmbeeOption):
    """
    Represents INP `mtype` elements.
    """

    _KEYWORD = 'mtype'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    kind = _field.Field(
        types.String, 'Multiplier type', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'flux', 'isotropic', 'population', 'reaction', 'source', 'track'}
    )

    _REGEX = re.compile(rf'\Amtype( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
