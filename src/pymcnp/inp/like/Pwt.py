import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Pwt(_field.Fields, _option.LikeOption):
    """
    Represents INP `pwt` elements.
    """

    _KEYWORD = 'pwt'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    weight = _field.Field(types.Real, 'Gets `weight`', required=True)

    _REGEX = re.compile(rf'\Apwt( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
