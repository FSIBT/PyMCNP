import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Psc(_field.Fields, _option.SsrOption):
    """
    Represents INP `psc` elements.
    """

    _KEYWORD = 'psc'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    constant = _field.Field(types.Real, 'Constant for approximation in PSC evaluation', required=True, invalid=lambda self, value: not value >= 0)

    _REGEX = re.compile(rf'\Apsc( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
