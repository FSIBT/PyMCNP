import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Kints(_field.Fields, _option.FmeshOption):
    """
    Represents INP `kints` elements.
    """

    _KEYWORD = 'kints'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    count = _field.Field.tuple(types.Integer, 'Number of mesh points z/theta for rectangular/cylindrical geometry', required=True, numeric=int)

    _REGEX = re.compile(rf'\Akints((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
