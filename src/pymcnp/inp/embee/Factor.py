import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Factor(_field.Fields, _option.EmbeeOption):
    """
    Represents INP `factor` elements.
    """

    _KEYWORD = 'factor'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    constant = _field.Field(types.Real, 'Multiplicative constant', required=True)

    _REGEX = re.compile(rf'\Afactor( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
