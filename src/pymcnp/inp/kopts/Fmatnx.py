import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Fmatnx(_field.Fields, _option.KoptsOption):
    """
    Represents INP `fmatnx` elements.
    """

    _KEYWORD = 'fmatnx'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    fmat_nx = _field.Field(types.Real, 'Fmat_nx', required=True)

    _REGEX = re.compile(rf'\Afmatnx( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
