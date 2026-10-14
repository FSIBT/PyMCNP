import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Emesh(_field.Fields, _option.FmeshOption):
    """
    Represents INP `emesh` elements.
    """

    _KEYWORD = 'emesh'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    energy = _field.Field(types.Real, 'Values of mesh points in energy', required=True)

    _REGEX = re.compile(rf'\Aemesh( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
