import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Tally(_field.Fields, _option.PtracOption):
    """
    Represents INP `tally` elements.
    """

    _KEYWORD = 'tally'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    numbers = _field.Field.tuple(types.Integer, 'List of tally numbers for filtering', required=True, numeric=int)

    _REGEX = re.compile(rf'\Atally((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
