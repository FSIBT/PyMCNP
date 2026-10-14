import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Shift(_field.Fields, _option.FmultOption):
    """
    Represents INP `shift` elements.
    """

    _KEYWORD = 'shift'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.Integer, 'Shift method setting', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1, 2, 3, 4})

    _REGEX = re.compile(rf'\Ashift( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
