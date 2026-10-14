import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Tbin(_field.Fields, _option.MplotOption):
    """
    Represents INP `tbin` elements.
    """

    _KEYWORD = 'tbin'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    n = _field.Field(types.Integer, 'Time bin to plot', required=True, numeric=int)

    _REGEX = re.compile(rf'\Atbin( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
