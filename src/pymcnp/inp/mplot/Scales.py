import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Scales(_field.Fields, _option.MplotOption):
    """
    Represents INP `scales` elements.
    """

    _KEYWORD = 'scales'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    n = _field.Field(types.Integer, 'Plot scale setting', required=True, numeric=int, invalid=lambda self, value: value not in {1, 2, 3})

    _REGEX = re.compile(rf'\Ascales( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
