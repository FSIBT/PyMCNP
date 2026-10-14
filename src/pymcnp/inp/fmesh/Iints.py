import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Iints(_field.Fields, _option.FmeshOption):
    """
    Represents INP `iints` elements.
    """

    _KEYWORD = 'iints'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    count = _field.Field.tuple(types.Integer, 'Number of mesh points x/r for rectangular/cylindrical geometry', required=True, numeric=int)

    _REGEX = re.compile(rf'\Aiints((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
