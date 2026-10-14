import re

from ... import _field
from . import _option
from .... import types
from .... import errors


class Niso(_field.Fields, _option.BlockOption):
    """
    Represents INP `niso` elements.
    """

    _KEYWORD = 'niso'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.Integer, 'Number of isotopes', required=True, numeric=int)

    _REGEX = re.compile(rf'\Aniso( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
