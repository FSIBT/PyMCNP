import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Fcl(_field.Fields, _option.CellOption):
    """
    Represents INP `fcl` elements.
    """

    _KEYWORD = 'fcl'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    designator = _field.Field(types.Designator, 'Cell particle designator', required=True, numeric=())
    control = _field.Field(types.Real, 'Cell forced-collision control', required=True, invalid=lambda self, value: not (value >= -1 and value <= 1))

    _REGEX = re.compile(rf'\Afcl:(\S+)( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
