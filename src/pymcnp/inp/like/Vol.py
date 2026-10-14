import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Vol(_field.Fields, _option.LikeOption):
    """
    Represents INP `vol` elements.
    """

    _KEYWORD = 'vol'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    volume = _field.Field(types.Real, 'Gets `volume`', required=True, invalid=lambda self, value: not value >= 0)

    _REGEX = re.compile(rf'\Avol( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
