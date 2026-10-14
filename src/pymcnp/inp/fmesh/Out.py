import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Out(_field.Fields, _option.FmeshOption):
    """
    Represents INP `out` elements.
    """

    _KEYWORD = 'out'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.String, 'Output format', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'col', 'cf', 'ij', 'ik', 'jk', 'none'})

    _REGEX = re.compile(rf'\Aout( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
