import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Tnorm(_field.Fields, _option.FmeshOption):
    """
    Represents INP `tnorm` elements.
    """

    _KEYWORD = 'tnorm'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.String, 'Tally results divided by time yes/no', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'yes', 'no'})

    _REGEX = re.compile(rf'\Atnorm( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
