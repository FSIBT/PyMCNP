import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Sfyield(_field.Fields, _option.FmultOption):
    """
    Represents INP `sfyield` elements.
    """

    _KEYWORD = 'sfyield'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    fission_yield = _field.Field(types.Real, 'Spontaneous fission yield', required=True)

    _REGEX = re.compile(rf'\Asfyield( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
