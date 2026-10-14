import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Pecut(_field.Fields, _option.ActOption):
    """
    Represents INP `pecut` elements.
    """

    _KEYWORD = 'pecut'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    cutoff = _field.Field(types.Real, 'Delayed-gamma energy cutoff', required=True)

    _REGEX = re.compile(rf'\Apecut( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
