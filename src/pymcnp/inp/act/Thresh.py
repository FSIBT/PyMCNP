import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Thresh(_field.Fields, _option.ActOption):
    """
    Represents INP `thresh` elements.
    """

    _KEYWORD = 'thresh'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    fraction = _field.Field(types.Real, 'Fraction of highest-amplitude discrete delayed-gamma lines retained', required=True, invalid=lambda self, value: not (value >= 0 and value <= 1))

    _REGEX = re.compile(rf'\Athresh( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
