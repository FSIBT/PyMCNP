import re

from .. import _field
from . import _option
from ... import types


class Vec(_field.Fields, _option.FmeshOption):
    """
    Represents INP `vec` elements.
    """

    _KEYWORD = 'vec'

    x = _field.Field(types.Real, 'Plane vector x component', required=True)
    y = _field.Field(types.Real, 'Plane vector y component', required=True)
    z = _field.Field(types.Real, 'Plane vector z component', required=True)

    _REGEX = re.compile(rf'\Avec( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
