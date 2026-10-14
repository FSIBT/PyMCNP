import re

from ... import _field
from . import _option
from .... import types
from .... import errors


class Iquad(_field.Fields, _option.BlockOption):
    """
    Represents INP `iquad` elements.
    """

    _KEYWORD = 'iquad'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.Integer, 'Quadrature', required=True, numeric=int, invalid=lambda self, value: value not in {1, 2, 3, 4, 5, 6, 7, 8, 9})

    _REGEX = re.compile(rf'\Aiquad( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
