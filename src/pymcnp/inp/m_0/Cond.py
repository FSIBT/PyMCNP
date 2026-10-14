import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Cond(_field.Fields, _option.MOption_0):
    """
    Represents INP `cond` elements.
    """

    _KEYWORD = 'cond'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.Real, 'Conduction state for EL03 electron-transport evaluation', required=True)

    _REGEX = re.compile(rf'\Acond( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
