import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Mat(_field.Fields, _option.LikeOption):
    """
    Represents INP `mat` elements.
    """

    _KEYWORD = 'mat'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    material = _field.Field(types.Integer, 'Gets `material`', required=True, numeric=int, invalid=lambda self, value: not 0 <= value <= 99999999)

    _REGEX = re.compile(rf'\Amat( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
