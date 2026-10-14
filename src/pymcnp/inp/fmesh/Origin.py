import re

from .. import _field
from . import _option
from ... import types


class Origin(_field.Fields, _option.FmeshOption):
    """
    Represents INP `origin` elements.
    """

    _KEYWORD = 'origin'

    x = _field.Field(types.Real, 'Origin x coordinate', required=True)
    y = _field.Field(types.Real, 'Origin y coordinate', required=True)
    z = _field.Field(types.Real, 'Origin z coordinate', required=True)

    _REGEX = re.compile(rf'\Aorigin( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
