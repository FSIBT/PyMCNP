import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Rr(_field.Fields, _option.VarOption):
    """
    Represents INP `rr` elements.
    """

    _KEYWORD = 'rr'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(
        types.String, 'Roulette game for weight windows and cell/energy/time importance off/no', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'no', 'off'}
    )

    _REGEX = re.compile(rf'\Arr( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
