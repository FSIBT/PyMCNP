import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Mat(_field.Fields, _option.EmbeeOption):
    """
    Represents INP `mat` elements.
    """

    _KEYWORD = 'mat'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    number = _field.Field(types.Integer, 'Material number', required=True, numeric=int, invalid=lambda self, value: not (value >= 0 and value <= 99999999))

    _REGEX = re.compile(rf'\Amat( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
