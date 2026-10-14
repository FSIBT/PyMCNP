import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Cos(_field.Fields, _option.KsenOption):
    """
    Represents INP `cos` elements.
    """

    _KEYWORD = 'cos'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    cosines = _field.Field.tuple(types.Real, 'Range of direction-change cosines', required=True)

    _REGEX = re.compile(rf'\Acos((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
