import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Wgt(_field.Fields, _option.SsrOption):
    """
    Represents INP `wgt` elements.
    """

    _KEYWORD = 'wgt'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    constant = _field.Field(types.Real, 'Particle weight multiplier', required=True)

    _REGEX = re.compile(rf'\Awgt( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
