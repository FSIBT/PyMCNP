import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Factor(_field.Fields, _option.FmeshOption):
    """
    Represents INP `factor` elements.
    """

    _KEYWORD = 'factor'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    multiple = _field.Field(types.Real, 'Multiplicative factor for each mesh', required=True)

    _REGEX = re.compile(rf'\Afactor( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
