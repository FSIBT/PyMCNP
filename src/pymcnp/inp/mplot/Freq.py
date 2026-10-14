import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Freq(_field.Fields, _option.MplotOption):
    """
    Represents INP `freq` elements.
    """

    _KEYWORD = 'freq'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    n = _field.Field(types.Integer, 'Number of histories between plotting calls', required=True, numeric=int)

    _REGEX = re.compile(rf'\Afreq( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
