import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Nonu(_field.Fields, _option.LikeOption):
    """
    Represents INP `nonu` elements.
    """

    _KEYWORD = 'nonu'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.Integer, 'Gets `setting`', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1, 2})

    _REGEX = re.compile(rf'\Anonu( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
