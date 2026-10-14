import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Vec_0(_field.Fields, _option.SdefOption):
    """
    Represents INP `vec` elements variation #0.
    """

    _KEYWORD = 'vec'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    x = _field.Field(types.Real, 'Reference vector for DIR x-component', required=True)
    y = _field.Field(types.Real, 'Reference vector for DIR y-component', required=True)
    z = _field.Field(types.Real, 'Reference vector for DIR z-component', required=True)

    _REGEX = re.compile(rf'\Avec( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
