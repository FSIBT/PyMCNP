import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Mt(_field.Fields, _option.KsenOption):
    """
    Represents INP `mt` elements.
    """

    _KEYWORD = 'mt'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    numbers = _field.Field.tuple(types.Integer, 'List of reaction numbers for pertubation', required=True, numeric=int)

    _REGEX = re.compile(rf'\Amt((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
