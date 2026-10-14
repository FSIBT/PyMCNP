import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class New(_field.Fields, _option.SsrOption):
    """
    Represents INP `new` elements.
    """

    _KEYWORD = 'new'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    numbers = _field.Field.tuple(types.Integer, 'Tuple of surface numbers to start run', required=True, numeric=int)

    _REGEX = re.compile(rf'\Anew((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
