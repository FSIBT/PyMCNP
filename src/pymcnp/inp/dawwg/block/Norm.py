import re

from ... import _field
from . import _option
from .... import types
from .... import errors


class Norm(_field.Fields, _option.BlockOption):
    """
    Represents INP `norm` elements.
    """

    _KEYWORD = 'norm'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.Real, 'Norm', required=True)

    _REGEX = re.compile(rf'\Anorm( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
