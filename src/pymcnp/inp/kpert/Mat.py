import re

from .. import _field
from . import _option
from ... import types


class Mat(_field.Fields, _option.KpertOption):
    """
    Represents INP `mat` elements.
    """

    _KEYWORD = 'mat'

    numbers = _field.Field.tuple(types.Integer, 'List of materials', required=True, numeric=int)

    _REGEX = re.compile(rf'\Amat((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
