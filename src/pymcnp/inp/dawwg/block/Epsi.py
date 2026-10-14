import re

from ... import _field
from . import _option
from .... import types
from .... import errors


class Epsi(_field.Fields, _option.BlockOption):
    """
    Represents INP `epsi` elements.
    """

    _KEYWORD = 'epsi'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.Real, 'Convergence precision', required=True)

    _REGEX = re.compile(rf'\Aepsi( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
