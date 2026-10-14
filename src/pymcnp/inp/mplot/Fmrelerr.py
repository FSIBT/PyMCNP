import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Fmrelerr(_field.Fields, _option.MplotOption):
    """
    Represents INP `fmrelerr` elements.
    """

    _KEYWORD = 'fmrelerr'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    n = _field.Field(types.Integer, 'Tally error to plot', required=True, numeric=int)

    _REGEX = re.compile(rf'\Afmrelerr( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
