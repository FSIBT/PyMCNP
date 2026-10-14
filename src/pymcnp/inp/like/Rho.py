import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Rho(_field.Fields, _option.LikeOption):
    """
    Represents INP `rho` elements.
    """

    _KEYWORD = 'rho'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    density = _field.Field(types.Real, 'Gets `density`', required=True)

    _REGEX = re.compile(rf'\Arho( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
