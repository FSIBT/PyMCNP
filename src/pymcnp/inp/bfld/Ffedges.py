import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Ffedges(_field.Fields, _option.BfldOption):
    """
    Represents INP `ffedges` elements.
    """

    _KEYWORD = 'ffedges'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    numbers = _field.Field.tuple(types.Real, 'Surface numbers to apply field fringe edges', required=True)

    _REGEX = re.compile(rf'\Affedges((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
