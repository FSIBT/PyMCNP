import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Erg(_field.Fields, _option.PertOption):
    """
    Represents INP `erg` elements.
    """

    _KEYWORD = 'erg'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    energy_lower_bound = _field.Field(types.Real, 'Lower bound for energy pertubation', required=True)
    energy_upper_bound = _field.Field(types.Real, 'Upper bound for energy pertubation', required=True)

    _REGEX = re.compile(rf'\Aerg( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
