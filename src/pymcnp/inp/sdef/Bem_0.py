import re

from .. import _field
from . import _option
from ... import types


class Bem_0(_field.Fields, _option.SdefOption):
    """
    Represents INP `bem` elements variation #0.
    """

    _KEYWORD = 'bem'

    exn = _field.Field(types.Real, 'Normalized beam emittance parameter for x coordinates', required=True)
    eyn = _field.Field(types.Real, 'Normalized beam emittance parameter for x coordinates', required=True)
    bml = _field.Field(types.Real, 'Distance from the aperture to the spot', required=True, invalid=lambda self, value: not value >= 0)

    _REGEX = re.compile(rf'\Abem( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
