import re

from ... import _field
from . import _option
from .... import types
from .... import errors


class Srcacc(_field.Fields, _option.BlockOption):
    """
    Represents INP `srcacc` elements.
    """

    _KEYWORD = 'srcacc'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.String, 'Transport accelerations', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'dsa', 'tsa', 'no'})

    _REGEX = re.compile(rf'\Asrcacc( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
