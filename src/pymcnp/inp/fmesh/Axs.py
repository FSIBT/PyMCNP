import re

from .. import _field
from . import _option
from ... import types


class Axs(_field.Fields, _option.FmeshOption):
    """
    Represents INP `axs` elements.
    """

    _KEYWORD = 'axs'

    x = _field.Field(types.Real, 'Cylindrical mesh axis vector x component', required=True)
    y = _field.Field(types.Real, 'Cylindrical mesh axis vector y component', required=True)
    z = _field.Field(types.Real, 'Cylindrical mesh axis vector z component', required=True)

    _REGEX = re.compile(rf'\Aaxs( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
