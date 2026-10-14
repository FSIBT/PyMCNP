import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Sfnu(_field.Fields, _option.FmultOption):
    """
    Represents INP `sfnu` elements.
    """

    _KEYWORD = 'sfnu'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    distribution = _field.Field.tuple(types.Real, 'V bar for or of cumulative distribution the sampling spontaneous fission', required=True)

    _REGEX = re.compile(rf'\Asfnu((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
